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
    int count, newton;
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
    int max_nonlinear_iterations = 1;
    IssmDouble eps_res, eps_rel, eps_abs;

    /*Recover parameters: */
    // femmodel->parameters->FindParam(&max_nonlinear_iterations,StressbalanceMaxiterEnum);
    femmodel->parameters->FindParam(&newton, StressbalanceIsnewtonEnum);
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

        /*Solver forward model*/
        if (count == 0 || newton == 2) {
            SystemMatricesx(&Kff, &Kfs, &pf, &df, nullptr, femmodel);
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

        // pJf = -pJf
        pJf->Scale(-1.0);
        // pJf = pJf + pf
        pJf->AXPY(pf, +1.0);

        _printf0_("running newton:" << count <<"\n");

        // v = uf
        // p = pf
        // G(v, p) = pJf

        CreateJacobianMatrixx(&Jff, femmodel, kmax);

        // Matrix<IssmDouble> *a = new Matrix<IssmDouble>(2, 2, false);
        //
        // MatSetOption(a->pmatrix->matrix, MAT_NEW_NONZERO_ALLOCATION_ERR, PETSC_FALSE);
        //
        // PetscScalar values[1] = {2};
        // a->SetZero();
        // IssmInt idxm = 0;
        // IssmInt idxn = 0;
        // a->SetValues(1, &idxm, 1, &idxn, values, INS_VAL);
        // values[0] = {1};
        // idxm = 1;
        // idxn = 1;
        // a->SetValues(1, &idxm, 1, &idxn, values, INS_VAL);
        // a->Assemble();
        //
        // Vector<IssmDouble> *b = new Vector<IssmDouble>(2);
        // b->SetValue(0, 5, INS_VAL);
        // b->SetValue(1, 32, INS_VAL);
        // b->Assemble();
        //
        // cout << "a:" << endl;
        // a->Echo();
        // cout << "b:" << endl;
        // b->Echo();
        //
        // Solver<IssmDouble> *solver = new Solver<IssmDouble>(a, b, nullptr, nullptr, femmodel->parameters);
        //
        // Vector<IssmDouble> *x = solver->Solve();
        //
        // IssmDouble y;
        // x->GetValue(&y, 0);
        // cout << "y = " << y << endl;
        // x->GetValue(&y, 1);
        // cout << "y = " << y << endl;

        // for (int i = 0; i < 3; i++) {
        //     cout << i << endl;
        // }

        // delete solver;



        // double min_term_old = minimization_term;


        // # We get the minimization term from the attributes
        // minimization_term = getattr(solver.equation,self.min_term)
        // # The derivative for the minimization term has the same name and additionally _derivative
        // minimization_derivative = getattr(solver.equation,self.min_term+str('_derivative'))
        // # We get the old value of the minimization term.
        // minimization_term_old = getattr(solver,self.min_term+str('_old'))
        // # We obtain the old minimization value, if we calculated it
        // if(np.isnan(minimization_term_old)):
        //     min_term_old = minimization_term()
        // else:
        //     min_term_old = minimization_term_old
        // gradient = minimization_derivative(U,1.0)
        //
        double minimization_term = pJf->Norm(NORM_TWO);

        double min_term_new;
        double min_term_old;
        double alpha = 1.0;
        double gamma = 1e-10;


        while (min_term_new > min_term_old - gamma * alpha * gradient and alpha > self.min_step) {
            alpha = 0.5 * alpha;
            solver.equation.U.assign(solver.equation.U + alpha * U);
            min_term_new = minimization_term();
        }

        // G'(x_n)(x_{n+1} - x_n) = -G(x_n)
        Solverx(&duf, Jff, pJf, nullptr, nullptr, femmodel->parameters);


        delete Jff;
        delete pJf;

        // stepsize a = 1

        // uf = uf + alpha * duf
        uf->AXPY(duf, alpha);


        delete duf;
        Mergesolutionfromftogx(&ug, uf, ys, femmodel->nodes, femmodel->parameters);
        delete ys;
        InputUpdateFromSolutionx(femmodel, ug);
        count++;

        /*Check convergence*/
        Kff->MatMult(uf, pJf);
        convergence(&converged, Kff, pf, uf, old_uf, eps_res, eps_rel, eps_abs);
        delete Kff;
        delete pf;
        if (converged == true) break;
        if (count >= max_nonlinear_iterations) {
            _printf0_("   maximum number of Newton iterations (" << max_nonlinear_iterations << ") exceeded\n");
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
