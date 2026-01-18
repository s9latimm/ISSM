/*!\file: solutionsequence_nonlinear.cpp
 * \brief: core of a non-linear solution, using fixed-point method 
 */

#include "./solutionsequences.h"
#include "../toolkits/toolkits.h"
#include "../classes/classes.h"
#include "../shared/shared.h"
#include "../modules/modules.h"

void solutionsequence_newton(FemModel *femmodel) {
    /*intermediary: */
    bool converged;
    int count, newton, maxiter;
    IssmDouble kmax;
    Matrix<IssmDouble> *Kff = nullptr;
    Matrix<IssmDouble> *Kfs = nullptr;
    Matrix<IssmDouble> *Jff = nullptr;
    Vector<IssmDouble> *ug = nullptr;
    Vector<IssmDouble> *old_ug = nullptr;
    Vector<IssmDouble> *uf = nullptr;
    Vector<IssmDouble> *old_uf = nullptr;
    Vector<IssmDouble> *duf = nullptr;
    Vector<IssmDouble> *pf = nullptr;
    Vector<IssmDouble> *pJf = nullptr;
    Vector<IssmDouble> *df = nullptr;
    Vector<IssmDouble> *ys = nullptr;

    /*parameters:*/
    IssmDouble eps_res, eps_rel, eps_abs;

    /*Recover parameters: */
    // femmodel->parameters->FindParam(&max_nonlinear_iterations,StressbalanceMaxiterEnum);
    femmodel->parameters->FindParam(&newton, StressbalanceIsnewtonEnum);
    femmodel->parameters->FindParam(&maxiter, StressbalanceMaxiterEnum);
    femmodel->parameters->FindParam(&eps_res, StressbalanceRestolEnum);
    femmodel->parameters->FindParam(&eps_rel, StressbalanceReltolEnum);
    femmodel->parameters->FindParam(&eps_abs, StressbalanceAbstolEnum);
    femmodel->UpdateConstraintsx();

    count = 0;
    converged = false;

    /*Start non-linear iteration using input velocity: */
    GetSolutionFromInputsx(&ug, femmodel);
    Reducevectorgtofx(&uf, ug, femmodel->nodes, femmodel->parameters);

    //Update once again the solution to make sure that vx and vxold are similar (for next step in transient or steadystate)
    InputUpdateFromConstantx(femmodel, converged, ConvergedEnum);
    InputUpdateFromSolutionx(femmodel, ug);

    for (;;) {
        delete old_ug;
        old_ug = ug;
        delete old_uf;
        old_uf = uf;

        switch (newton) {
            case 1:
                _printf0_("running newton with fixed stepsize\n");
                break;
            case 3:
                _printf0_("running newton with adaptive stepsize\n");
                break;
            default: ;
        }

        if (count == 0 || newton == 2) {
            _printf0_("Initial picard iteration\n");

            SystemMatricesx(&Kff, &Kfs, &pf, &df,NULL, femmodel);
            CreateNodalConstraintsx(&ys, femmodel->nodes);
            Reduceloadx(pf, Kfs, ys);
            delete Kfs;
            femmodel->profiler->Start(SOLVER);
            Solverx(&uf, Kff, pf, old_uf, df, femmodel->parameters);
            delete df;
            delete Kff;
            delete pf;
            femmodel->profiler->Stop(SOLVER);
            Mergesolutionfromftogx(&ug, uf, ys, femmodel->nodes, femmodel->parameters);
            delete ys;
            InputUpdateFromSolutionx(femmodel, ug);
            delete old_ug;
            old_ug = ug;
            delete old_uf;
            old_uf = uf;
        }
        uf = old_uf->Duplicate();
        old_uf->Copy(uf);

        /*Prepare next iteration using Newton's method*/
        SystemMatricesx(&Kff, &Kfs, &pf, &df, &kmax, femmodel);
        delete df;
        CreateNodalConstraintsx(&ys, femmodel->nodes);
        Reduceloadx(pf, Kfs, ys);
        delete Kfs;

        pJf = pf->Duplicate();

        // pJf = Kff * uf
        Kff->MatMult(uf, pJf);

        // pJf = -pJf
        pJf->Scale(-1.0);

        // pJf = pJf + pf
        pJf->AXPY(pf, +1.0);

        CreateJacobianMatrixx(&Jff, femmodel, kmax);

        // G'(v_k, p_k)(w_k, q_k) = -G(v_k, p_k)
        // G(v_k, p_k) -> -(Kff * uf) + pf
        // Jff(duf) = pJf
        Solverx(&duf, Jff, pJf, nullptr, nullptr, femmodel->parameters);

        if (newton == 1) {
            uf->AXPY(duf, 1);
        } else if (newton == 4) {
            uf->AXPY(duf, .5);
        } else if (newton == 3) {
            // uf = uf + duf
            // uf->AXPY(duf, 1);

            double alpha = 1.;
            double gamma = 1e-10;

            pJf->Scale(-1.0);

            Vector<IssmDouble> *fu = pJf->Duplicate();
            Kff->MatMult(old_uf, fu);
            IssmDouble min_term_old = fu->Norm(NORM_TWO);
            IssmDouble min_term_new = -1;

            // ||G^T() * G()||
            // G'(v_k, p_k)(w_k, q_k)^T * G(v_k, p_k)
            // Jff->pmatrix->matrix.Transpose().MatMult(pJf, ?);
            // min_term_old ** 2

            Vector<IssmDouble> *gf = pJf->Duplicate();
            Jff->MatMult(duf, gf);
            double gradient = gf->Norm(NORM_TWO);

            int max_steps = 0;
            do {
                // uf = upf
                old_uf->Copy(uf);

                // u = u + alpha * duf
                uf->AXPY(duf, alpha);

                // pJf = Kff * u
                Kff->MatMult(uf, pJf);

                min_term_new = pJf->Norm(NORM_TWO);

                alpha = .5 * alpha;
                ++max_steps;
                _printf0_(
                    "step (" << max_steps <<"): "<< min_term_new << " < "\
                    << min_term_old << " - "<< gamma<< " * "<< alpha << " * "<< gradient << "\n");
            } while (min_term_new > min_term_old - gamma * alpha * gradient && max_steps < 100);
        }

        delete Jff;
        delete pJf;
        delete duf;
        Mergesolutionfromftogx(&ug, uf, ys, femmodel->nodes, femmodel->parameters);
        delete ys;
        InputUpdateFromSolutionx(femmodel, ug);
        count++;

        /*Check convergence*/
        // convergence(&converged, Kff, pf, uf, old_uf, eps_res, eps_rel, eps_abs);
        // delete Kff;
        // delete pf;
        // if (converged == true) break;
        if (count >= maxiter) {
            _printf0_("   maximum number of Newton iterations (" << maxiter << ") exceeded\n");
            break;
        }
    }

    if (VerboseConvergence())
        _printf0_("\n   total number of iterations: " << count << "\n");
    femmodel->results->AddResult(
        new GenericExternalResult<int>(femmodel->results->Size() + 1, StressbalanceConvergenceNumStepsEnum, count));

    /*clean-up*/
    delete uf;
    delete ug;
    delete old_ug;
    delete old_uf;
}
