//
// Hidden Markov Model program for written English
//
// Consistent with "Revealing Introduction" version dated January 12, 2017
//
// The program reads in data (English text) ignoring
// all punctuation, leaving only 26 letters and
// word spaces. Consequently, the A matrix is N x N and 
// the B matrix is N x M, where M = 27. The program
// begins with random (approximately uniform) A, B and pi,
// then attempts to climb to the optimal A and B.
// This program implements the work described in 
// Cave and Neuwirth's paper "Hiddsen Markov Models
// for English"
//
// Note: The data file must not have any formatting!
//
// To compile: gcc -o hmm hmm.c -O3
//

#include "q11.h"

// Importing stdlib for generating random integer
#include<stdlib.h>
#include<time.h>

int randomSubstitution = 0;

// generating the digraph. part c - question 11. 
void generate_English_diGraph(double A[][N],
        struct stepStruct *step,
        int T
        ){
        
        for(int i = 0 ; i < 26 ; i++)
            for(int j = 0 ; j < 26 ; j++)
                A[i][j] = 0.0;

        for(int i = 0 ; i < 2 ; i++)
            for(int t = 1 ; t < T ; t++)
                A[step[t-1].obs][step[t].obs]++;

        // Adding 5 and Normalizing
        for(int i = 0 ; i < 26 ; i++){
            
            double row_sum = 0.0;
            for(int j = 0 ; j < 26 ; j++){
                row_sum += A[i][j];
            }    
            row_sum += 130;

            double row_sto = 0.0;
            for(int j = 0 ; j < 26 ; j++){
                A[i][j] = (A[i][j] + 5) / row_sum;
                row_sto += A[i][j];
            }
            printf("\n The sum for row %d is %f", i+1, row_sto);
        }
        /* For Printing the new Matrix A
        printf("\n\nThe New A Matrix \n\n");
        for(int i = 0 ; i < 26 ; i++){
            for(int j = 0 ; j < 26 ; j++)
                printf("%f\t", A[i][j]);
            printf("\n");
        }
        */
        printf("\n\n");
}

int main(int argc, const char *argv[])
{
    int startPos,
        startChar,
        maxChars,
        maxIters,
        i,
        j,
        T,
        iter;
        
    int seed;

    double logProb,
           newLogProb;

    double pi[N],
           piBar[N],
           A[N][N],
           Abar[N][N],
           B[N][M],
           Bbar[N][M];
           
    char fname[80];
    
    struct stepStruct *step;

    srand(time(NULL));

    if(argc !=7)
    {
oops:   fprintf(stderr, "\nUsage: %s filename startPos startChar maxChars maxIters seed\n\n", argv[0]);
        fprintf(stderr, "where filename == input file\n");
        fprintf(stderr, "      startPos == starting position for each line (numbered from 0)\n");
        fprintf(stderr, "      startChar == starting character in file (numbered from 0)\n");
        fprintf(stderr, "      maxChars == max characters to read (<= 0 to read all)\n");
        fprintf(stderr, "      maxIters == max iterations of re-estimation algorithm\n");
        fprintf(stderr, "      seed == seed value for pseudo-random number generator (PRNG)\n\n");
        fprintf(stderr, "For example:\n\n      %s datafile 0 0 0 100 1241\n\n", argv[0]);
        fprintf(stderr, "will read all of `datafile' and perform a maximum of 100 iterations.\n\n");
        fprintf(stderr, "For the English text example, try:\n\n      %s BrownCorpus 15 1000 50000 200 22761\n\n", argv[0]);
        fprintf(stderr, "will read from `BrownCorpus' and seed the PRNG with 22761,\n");
        fprintf(stderr, "will not read characters 0 thru 14 of each new line in `BrownCorpus',\n");
        fprintf(stderr, "will not save the first 1000 characters read and\n");
        fprintf(stderr, "will save a maximum of 50k observations.\n\n");
        exit(0);
    }

//    sprintf(fname, argv[1]);
    strcpy(fname, argv[1]);
    startPos = atoi(argv[2]);
    startChar = atoi(argv[3]);
    maxChars = atoi(argv[4]);
    maxIters = atoi(argv[5]);
    seed = atoi(argv[6]);

    ////////////////////////
    // read the data file //
    ////////////////////////
    
    // determine number of observations
    printf("GetT... ");
    fflush(stdout);
    T = GetT(fname, 
             startPos,
             startChar,
             maxChars);
    
    printf("T = %d\n", T);

    // allocate memory
    printf("allocating %lu bytes of memory... ", (T + 1) * sizeof(struct stepStruct));
    fflush(stdout);
    if((step = calloc(T + 1, sizeof(struct stepStruct))) == NULL)
    {
        fprintf(stderr, "\nUnable to allocate alpha\n\n");
        exit(0);
    }
    printf("done\n");

    // read in the observations from file
    printf("GetObservations... ");
    fflush(stdout);
    T = GetObservations(fname, 
                        step, 
                        T,
                        startPos,
                        startChar,
                        maxChars,
                        0);

    printf("T = %d\n", T);

    // The new A
    generate_English_diGraph(A, step, T);

    /////////////////////////
    // hidden markov model //
    /////////////////////////

    srandom(seed);
    
    // initialize pi[], A[][] and B[][]
    initMatrices(pi, B, seed);

    // generating the cipher text
    T = GetObservations(fname, 
                        step, 
                        T,
                        startPos,
                        1000,
                        maxChars,
                        1);

    // We only need to consider first 1000 characters of the cipher text. So updating T to 1000
    T = 1000;

    // print pi[], A[][] and B[][] transpose
    printf("\nN = %d, M = %d, T = %d\n", N, M, T);
    printf("initial pi =\n");
    printPi(pi);
    printf("initial A =\n");
    printA(A);
    printf("initial B^T =\n");
    printBT(B);

    // initialization
    iter = 0;
    logProb = -1.0;
    newLogProb = 0.0;

    // main loop
    //while((iter < maxIters) && (newLogProb > logProb))
    while(iter < maxIters)
    {
        printf("\nbegin iteration = %d\n", iter);

        logProb = newLogProb;

        // alpha (or forward) pass
        printf("alpha pass... ");
        fflush(stdout);
        alphaPass(step, pi, A, B, T);
        printf("done\n");
        
        // beta (or backwards) pass
        printf("beta pass... ");
        fflush(stdout);
        betaPass(step, pi, A, B, T);
        printf("done\n");
        
        // compute gamma's and diGamma's
        printf("compute gamma's and diGamma's... ");
        fflush(stdout);
        computeGammas(step, pi, A, B, T);
        printf("done\n");
        
        // find piBar, reestimate of pi
        printf("reestimate pi... ");
        fflush(stdout);
        reestimatePi(step, piBar);
        printf("done\n");
        
        // find Abar, reestimate of A
        // reestimating of A is not required for question 11 d, so commenting out the code
        /*
        printf("reestimate A... ");
        fflush(stdout);
        reestimateA(step, Abar, T);
        printf("done\n");
        */
        
        // find Bbar, reestimate of B
        printf("reestimate B... ");
        fflush(stdout);
        reestimateB(step, Bbar, T);
        printf("done\n");
        
#ifdef PRINT_REESTIMATES
        printf("piBar =\n");
        printPi(piBar);
        printf("Abar =\n");
        printA(Abar);
        printf("Bbar^T = \n");
        printBT(Bbar);
#endif // PRINT_REESTIMATES

        // assign pi, A and B corresponding "bar" values
        for(i = 0; i < N; ++i)
        {
            pi[i] = piBar[i];
        
            /*
            for(j = 0; j < N; ++j)
            {
                A[i][j] = Abar[i][j];
            }
            */

            for(j = 0; j < M; ++j)
            {
                B[i][j] = Bbar[i][j];
            }
            
        }// next i

        // compute log [P(observations | lambda)], where lambda = (A,B,pi)
        newLogProb = 0.0;
        for(i = 0; i < T; ++i)
        {
            newLogProb += log(step[i].c);
        }
        newLogProb = -newLogProb;

        // a little trick so that no initial logProb is required
        if(iter == 0)
        {
            logProb = newLogProb - 1.0;
        }

        printf("completed iteration = %d, log [P(observation | lambda)] = %f\n", 
                iter, newLogProb);

        ++iter;

    }// end while
    
    printf("\nT = %d, N = %d, M = %d, iterations = %d\n\n", T, N, M, iter);
    printf("final pi =\n");
    printPi(pi);
    printf("\nfinal A =\n");
    printA(A);
    printf("\nfinal B^T =\n");
    printBT(B);
    printf("\nlog [P(observations | lambda)] = %f\n\n", newLogProb);

    // Calculating the Putative Key part of the problem - part d Question 11
    int count = 0;
    for(int i = 0 ; i < N ; i++){
        double max = B[i][0];
        int elem = 0;
        for(int j = 1 ; j < M ; j++){
            if(B[i][j] > max){
                max = B[i][j];
                elem = j;
            }
        }
        printf("\nThe %c element is mapped to %c", i+97, elem+97);
        if(elem == ((i + randomSubstitution) % 26))
            count++;
    }
    printf("\n\n\nThe key is %d\n\n", randomSubstitution);
    printf("\nFinal Count value: %d", count);
    double percentage = (double) count / N;
    printf("\nThe percentage is %0.4f\n\n", percentage);
}// end hmm


//
// alpha pass (or forward pass) including scaling
//
void alphaPass(struct stepStruct *step,
               double pi[], 
               double A[][N],
               double B[][M],
               int T)
{
    int i,
        j,
        t;
        
    double ftemp;
    
    // compute alpha[0]'s
    ftemp = 0.0;
    for(i = 0; i < N; ++i)
    {
        step[0].alpha[i] = pi[i] * B[i][step[0].obs];
        ftemp += step[0].alpha[i];
    }
    step[0].c = 1.0 / ftemp;

    // scale alpha[0]'s
    for(i = 0; i < N; ++i)
    {
        step[0].alpha[i] /= ftemp;
    }

    // alpha pass
    for(t = 1; t < T; ++t)
    {
        ftemp = 0.0;
        for(i = 0; i < N; ++i)
        {
            step[t].alpha[i] = 0.0;
            for(j = 0; j < N; ++j)
            {
                step[t].alpha[i] += step[t - 1].alpha[j] * A[j][i];
            }
            step[t].alpha[i] *= B[i][step[t].obs];
            ftemp += step[t].alpha[i];
        }
        step[t].c = 1.0 / ftemp;
        
        // scale alpha's
        for(i = 0; i < N; ++i)
        {
            step[t].alpha[i] /= ftemp;
        }
    
    }// next t
    
}// end alphaPass


//
// beta pass (or backwards pass) including scaling
//
void betaPass(struct stepStruct *step,
              double pi[], 
              double A[][N],
              double B[][M],
              int T)
{
    int i,
        j,
        t;

    // compute scaled beta[T - 1]'s
    for(i = 0; i < N; ++i)
    {
        step[T - 1].beta[i] = 1.0 * step[T - 1].c;
    }

    // beta pass
    for(t = T - 2; t >= 0; --t)
    {
        for(i = 0; i < N; ++i)
        {
            step[t].beta[i] = 0.0;
            for(j = 0; j < N; ++j)
            {
                step[t].beta[i] += A[i][j] * B[j][step[t + 1].obs] * step[t + 1].beta[j];
            }
            
            // scale beta's (same scale factor as alpha's)
            step[t].beta[i] *= step[t].c;
        }

    }// next t
        
}// end betaPass


//
// compute gamma's and diGamma's including optional error checking
//
void computeGammas(struct stepStruct *step,
                   double pi[], 
                   double A[][N],
                   double B[][M],
                   int T)
{
    int i,
        j,
        t;
        
    double denom;

#ifdef CHECK_GAMMAS
    double ftemp,
           ftemp2;
#endif // CHECK_GAMMAS

    // compute gamma's and diGamma's
    for(t = 0; t < T - 1; ++t)// t = 0,1,2,...,T-2
    {
        
#ifdef CHECK_GAMMAS
        ftemp2 = 0.0;
#endif // CHECK_GAMMAS

        for(i = 0; i < N; ++i)
        {
            step[t].gamma[i] = 0.0;
            for(j = 0; j < N; ++j)
            {
                step[t].diGamma[i][j] = (step[t].alpha[i] * A[i][j] * B[j][step[t + 1].obs] * step[t + 1].beta[j]);
                step[t].gamma[i] += step[t].diGamma[i][j];
            }

#ifdef CHECK_GAMMAS
            // verify that gamma[i] == alpha[i]*beta[i] / sum(alpha[j]*beta[j])
            ftemp2 += step[t].gamma[i];
            ftemp = 0.0;
            for(j = 0; j < N; ++j)
            {
                ftemp += step[t].alpha[j] * step[t].beta[j];
            }
            ftemp = (step[t].alpha[i] * step[t].beta[i]) / ftemp;
            if(DABS(ftemp - step[t].gamma[i]) > EPSILON)
            {
                printf("gamma[%d] = %f (%f) ", i, step[t].gamma[i], ftemp);
                printf("********** Error !!!\n");
            }
#endif // CHECK_GAMMAS

        }// next i
            
#ifdef CHECK_GAMMAS
        if(DABS(1.0 - ftemp2) > EPSILON)
        {
            printf("sum of gamma's = %f (should sum to 1.0)\n", ftemp2);
        }
#endif // CHECK_GAMMAS
            
    }// next t
    
    // special case for t = T-1
    for(j = 0; j < N; ++j)
    {
        step[T-1].gamma[j] = step[T-1].alpha[j];
    }

}// end computeGammas


//
// reestimate pi, the initial distribution
//
void reestimatePi(struct stepStruct *step, 
                  double piBar[])
{
    int i;
    
    // reestimate pi[]        
    for(i = 0; i < N; ++i)
    {
        piBar[i] = step[0].gamma[i];
    }
        
}// end reestimatePi


//
// reestimate the A matrix
//
void reestimateA(struct stepStruct *step, 
                 double Abar[][N], 
                 int T)
{
    int i,
        j,
        t;
    
    double numer,
           denom;
           
    // reestimate A[][]
    for(i = 0; i < N; ++i)
    {
        for(j = 0; j < N; ++j)
        {
            numer = denom = 0.0;

            // t = 0,1,2,...,T-2
            for(t = 0; t < T - 1; ++t)
            {
                numer += step[t].diGamma[i][j];
                denom += step[t].gamma[i];
                
            }// next t

            Abar[i][j] = numer / denom;
        
        }// next j
        
    }// next i
        
} // end reestimateA    


//
// reestimate the B matrix
//
void reestimateB(struct stepStruct *step, 
                 double Bbar[][M], 
                 int T)
{
    int i,
        j,
        t;
    
    double numer,
           denom;
           
    // reestimate B[][]
    for(i = 0; i < N; ++i)
    {
        for(j = 0; j < M; ++j)
        {
            numer = denom = 0.0;

            // t = 0,1,2,...,T-1
            for(t = 0; t < T; ++t)
            {
                if(step[t].obs == j)
                {
                    numer += step[t].gamma[i];
                }
                denom += step[t].gamma[i];

            }// next t

            Bbar[i][j] = numer / denom;
        
        }// next j
        
    }// next i
        
}// end reestimateB


//
// initialize pi[], A[][] and B[][]
//
void initMatrices(double pi[], 
                  double B[][M],
                  int seed)
{
    int i,
        j;
        
    double prob,
           ftemp,
           ftemp2;
    
    // initialize pseudo-random number generator
    srandom(seed);

    // initialize pi
    prob = 1.0 / (double)N;
    ftemp = prob / 10.0;
    ftemp2 = 0.0;
    for(i = 0; i < N; ++i)
    {
        if((random() & 0x1) == 0)
        {
            pi[i] = prob + (double)(random() & 0x7) / 8.0 * ftemp;
        }
        else
        {
            pi[i] = prob - (double)(random() & 0x7) / 8.0 * ftemp;
        }
        ftemp2 += pi[i];
        
    }// next i
    
    for(i = 0; i < N; ++i)
    {
        pi[i] /= ftemp2;
    }
    
    // initialize B[][]
    prob = 1.0 / (double)M;
    ftemp = prob / 10.0;
    for(i = 0; i < N; ++i)
    {
        ftemp2 = 0.0;
        for(j = 0; j < M; ++j)
        {
            if((random() & 0x1) == 0)
            {
                B[i][j] = prob + (double)(random() & 0x7) / 8.0 * ftemp;
            }
            else
            {
                B[i][j] = prob - (double)(random() & 0x7) / 8.0 * ftemp;
            }
            ftemp2 += B[i][j];
            
        }// next j
        
        for(j = 0; j < M; ++j)
        {
            B[i][j] /= ftemp2;
        }
        
    }// next i
    
}// end initMatrices


//
// read (but don't save) observations get T
//
int GetT(char fname[],
         int startPos,
         int startChar,
         int maxChars)
{
    FILE *in;

    int T,
        i,
        j,
        len,
        thisStartPos,
        totalNum,
        num;
        
    char temp[MAX_CHARS + 1];
    
    char space[1] = {" "};
    
    char alphabet[M] = ALPHABET;

    in = fopen(fname, "r");
    if(in == NULL)
    {
        fprintf(stderr, "\nError opening file %s\n\n", fname);
        exit(0);
    }
    
#ifdef PRINT_GET_T
    printf("\n");
#endif // PRINT_GET_T

    // count 'em
    totalNum = num = 0;
    while(fgets(temp, MAX_CHARS, in) != NULL)
    {
        len = strlen(temp);

        // each line should end with a single space
        while((strncmp(&temp[len - 1], space, 1) == 0) && (len > 0))
        {
            --len;
        }

        strncpy(&temp[len], space, 1);
        
        thisStartPos = startPos;
        
        // ignore leading spaces
        while((strncmp(&temp[thisStartPos], space, 1) == 0) && (thisStartPos < len))
        {
            ++thisStartPos;
        }
        
        for(i = thisStartPos; i <= len; ++i)
        {
            // find alphabetic characters, ignoring case
            // also drop all non-alphabet characters other than space
            for(j = 0; j < M; ++j)
            {
                if(strncasecmp(&temp[i], &alphabet[j], 1) == 0)
                {
                    ++totalNum;
                    if(totalNum >= startChar)
                    {
#ifdef PRINT_GET_T
                        printf("%c %d\n", alphabet[j], num);
#endif // PRINT_GET_T
                        ++num;
                        if((maxChars > 0) && (num >= maxChars))
                        {
                            return(num);
                        }
                        
                    }// end if
                    
                    break;
                    
                }// end if
                
            }// next j

        }// next i
                
    }// end while
    
    fclose(in);

    return(num);

}// end GetT


//
// read and save observations
//
int GetObservations(char fname[], 
                    struct stepStruct *step,
                    int T,
                    int startPos,
                    int startChar,
                    int maxChars,
                    int flag)
{
    FILE *in;

    int i,
        j,
        len,
        num,
        thisStartPos,
        totalNum;
        
    char temp[MAX_CHARS + 2];
    
    char space[1] = {" "};
    
    char alphabet[M] = ALPHABET;
    
    // Part a - Question 11. Encrypting the key
    randomSubstitution = 0;
    if (flag == 1)
    {
        while(randomSubstitution == 0){
            randomSubstitution = rand() % 10;
        }
    }

    in = fopen(fname, "r");
    if(in == NULL)
    {
        fprintf(stderr, "\nError opening file %s\n\n", fname);
        exit(0);
    }
    
#ifdef PRINT_OBS
    printf("\n");
#endif // PRINT_OBS

    // read 'em in
    totalNum = num = 0;
    while(fgets(temp, MAX_CHARS, in) != NULL)
    {
        len = strlen(temp);
        
        // each line should end with a single space
        while((strncmp(&temp[len - 1], space, 1) == 0) && (len > 0))
        {
            --len;
        }
        strncpy(&temp[len], space, 1);
        
        thisStartPos = startPos;
        
        // ignore leading spaces
        while((strncmp(&temp[thisStartPos], space, 1) == 0) && (thisStartPos < len))
        {
            ++thisStartPos;
        }

        for(i = thisStartPos; i <= len; ++i)
        {
            // find alphabetic characters, ignoring case,
            // drop all non-alphabet characters other than space 
            for(j = 0; j < M; ++j)
            {
                if(strncasecmp(&temp[i], &alphabet[j], 1) == 0)
                {
                    ++totalNum;
                    if(totalNum >= startChar)
                    {
                        if(flag == 1)
                            step[num].obs = (j + randomSubstitution) % 26;
                        else
                            step[num].obs = j;
                        
                        
#ifdef PRINT_OBS
                        printf("%c %d\n", alphabet[j], step[num].obs);
#endif // PRINT_OBS
                        ++num;
                        if(num > T)
                        {
                            printf("\nError --- T exceeded in GetObservations()\n\n");
                            exit(0);
                        }
                        if((maxChars > 0) && (num >= maxChars))
                        {
                            return(num);
                        }
                        
                    }// end if
                    
                    break;
                    
                }// end if
                
            }// next j

        }// next i

    }// end while
    
    fclose(in);

    return(num);

}// end GetObservations


//
// print pi[]
//
void printPi(double pi[])
{
    int i;
        
    double ftemp;

    ftemp = 0.0;
    for(i = 0; i < N; ++i)
    {
        printf("%8.5f ", pi[i]);
        ftemp += pi[i];
    }
    printf(",  sum = %f\n", ftemp);

}// end printPi


//
// print A[][]
//
void printA(double A[][N])
{
    int i,
        j;
        
    double ftemp;

    for(i = 0; i < N; ++i)
    {
        ftemp = 0.0;
        for(j = 0; j < N; ++j)
        {
            printf("%8.5f ", A[i][j]);
            ftemp += A[i][j];
        }
        printf(",  sum = %f\n", ftemp);
        
    }// next i

}// end printA


//
// print BT[][]
//
void printBT(double B[][M])
{
    int i,
        j;
        
    double ftemp;
    
    char alphabet[M] = ALPHABET;
    
    for(i = 0; i < M; ++i)
    {
        printf("%c ", alphabet[i]);
        for(j = 0; j < N; ++j)
        {
            printf("%8.5f ", B[j][i]);
        }
        printf("\n");
    }
    for(i = 0; i < N; ++i)
    {
        ftemp = 0.0;
        for(j = 0; j < M; ++j)
        {
            ftemp += B[i][j];
        }
        printf("sum[%d] = %f ", i, ftemp);
    }
    printf("\n");

}// end printB
