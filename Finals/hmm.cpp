#include <stdio.h>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <string>
#include <fstream>
#include <string.h>
#include "hmm.h"

//#define USE_FIXED_DIGRAPH //enable this define to use a fixed A matrix from a pre-defined digraph
#ifdef USE_FIXED_DIGRAPH
#include "AMat.h"
#endif

#define MAX_INT 9223372036854775807

//#define GRAD_DESCENT //define this to use gradient descent to train
#define TEMP 1.0
#define LEARNING_RATE 1.0




HMM::HMM(int N, int M, int minIters, float epsilon)
{
   mN = N;
   mM = M;
   mMinIters = minIters;
   mEps = epsilon;
   mOldLogProb = -MAX_INT;

   mA = NULL;
   mB = NULL;
   mPI = NULL;

   mC = NULL;
   mAlpha = NULL;
   mBeta = NULL;
   mGamma = NULL;
   mDiGamma = NULL;

   mW = NULL;
   mV = NULL;
}
HMM::~HMM()
{
   freeTables();
}

void HMM::freeTables()
{
   if (mA) {
      free(mA);
      mA = NULL;
   }
   if (mB) {
      free(mB);
      mB = NULL;
   }
   if (mPI) {
      free(mPI);
      mPI = NULL;
   }
   if (mC) {
      free(mC);
      mC = NULL;
   }
   if (mAlpha) {
      free(mAlpha);
      mAlpha = NULL;
   }
   if (mBeta) {
      free(mBeta);
      mBeta = NULL;
   }
   if (mGamma) {
      free(mGamma);
      mGamma = NULL;
   }
   if (mDiGamma) {
      free(mDiGamma);
      mDiGamma = NULL;
   }
   if (mW) {
      free(mW);
      mW = NULL;
   }
   if (mV) {
      free(mV);
      mV = NULL;
   }
}

void HMM::printModel()
{
   printf("A = {\n");
   for (int i = 0; i < mN; i++) {
      std::string msg = std::to_string(i) + ": [";
      for (int j = 0; j < mN; j++) {
         msg += std::to_string(*getA(i, j)) + ", ";
      }
      msg += "],";
      printf("%s\n", msg.c_str());
   }
   printf("}\n");
   printf("B = \n");
   for (int j = 0; j < mM; j++) {
      std::string msg = std::to_string(j) + ": ";
      for (int i = 0; i < mN; i++) {
         msg += std::to_string(*getB(i, j)) + " ";
      }
      printf("%s\n", msg.c_str());
   }
   printf("PI = \n");
   std::string msg = "";
   for (int i = 0; i < mN; i++) {
      msg += std::to_string(*getPI(i)) + " ";
   }
   printf("%s\n", msg.c_str());
}

void HMM::fit(int* obserArr, int T)
{
   int iters = 0;
   float logProb = -MAX_INT;
   float diff = MAX_INT;
   setupTable(T);
   randomInit();
#ifndef _NO_MAIN
   printModel();
#endif
   while (iters < mMinIters || diff > mEps) {
      logProb = getScore(obserArr, T);
      backwardPass(obserArr, T);
      calcGammaDigamma(obserArr, T);
      reEstimateModel(obserArr, T);

      diff = std::abs(logProb - mOldLogProb); 
      mOldLogProb = logProb;

      //if (iters % 10 == 0) {
#ifndef _NO_MAIN
         printModel();
         printf("%d_score = %.3f\n========================================\n\n", iters, logProb);
#endif
      //}

      iters += 1;
   }

   printf("HMM trained\n");
#ifndef _NO_MAIN
   printModel();
#endif
   printf("%d_score = %.3f\n========================================\n\n", iters, logProb);
}

float HMM::getScore(int* obserArr, int T)
{
   forwardPass(obserArr, T);
   float logProb = 0;
   for (int t = 0; t < T; t++) { 
      float l = std::log(*(getC(t))); 
      if (!std::isnan(l)) logProb += l; 
      else logProb += -MAX_INT;
   }
   return -logProb;
}

void HMM::setupTable(int T)
{
   freeTables();

#ifndef USE_FIXED_DIGRAPH
   mA = (float*)malloc(mN*mN*sizeof(float));
   if (!mA) {
      printf("No memory!\n");
      exit(-1);
   }
#endif

   mB = (float*)malloc(mN*mM*sizeof(float));
   if (!mB) {
      printf("No memory!\n");
      exit(-1);
   }
   mPI = (float*)malloc(mN*sizeof(float));
   if (!mPI) {
      printf("No memory!\n");
      exit(-1);
   }

   mC = (float*)malloc(T*sizeof(float));
   if (!mC) {
      printf("No memory!\n");
      exit(-1);
   }
   mAlpha = (float*)malloc(T*mN*sizeof(float));
   if (!mAlpha) {
      printf("No memory!\n");
      exit(-1);
   }
   mBeta = (float*)malloc(T*mN*sizeof(float));
   if (!mBeta) {
      printf("No memory!\n");
      exit(-1);
   }
   mGamma = (float*)malloc(T*mN*sizeof(float));
   if (!mGamma) {
      printf("No memory!\n");
      exit(-1);
   }
   mDiGamma = (float*)malloc(T*mN*mN*sizeof(float));
   if (!mDiGamma) {
      printf("No memory!\n");
      exit(-1);
   }

   mW = (float*)malloc(mN*mN*sizeof(float));
   if (!mW) {
      printf("No memory!\n");
      exit(-1);
   }

   mV = (float*)malloc(mN*mM*sizeof(float));
   if (!mV) {
      printf("No memory!\n");
      exit(-1);
   }
}
float HMM::getRandVal(int k)
{
   float r = float(rand())/RAND_MAX;
   float v = 1.0/k; 
   float delta = 0.1 * v;
   return v + -delta + (r * 2 * delta);
} 

void HMM::normalizeArr(float* arr, int T)
{
   float sum = 0;
   for (int idx = 0; idx < T; idx++) sum += arr[idx];
   if (sum == 0) {
      printf("error! can't normalize all 0\n");
      exit(-1);
   }
   for (int idx = 0; idx < T; idx++) arr[idx] /= sum;
}
void HMM::randomInit()
{
   srand(time(NULL));

#ifndef USE_FIXED_DIGRAPH
   for (int idx = 0; idx < mN; idx++) {
      for (int jdx = 0; jdx < mN; jdx++) {
         *getA(idx, jdx) = getRandVal(mN);

         //init weights
         float r = float(rand())/RAND_MAX;
         *getW(idx, jdx) = r*2.0 - 1.0;
      }
      normalizeArr(mA+(idx*mN), mN);
   }
#endif

   for (int idx = 0; idx < mN; idx++) {
      for (int jdx = 0; jdx < mM; jdx++) {
         *getB(idx, jdx) = getRandVal(mM);
         //init weights
         float r = float(rand())/RAND_MAX;
         *getV(idx, jdx) = r*2.0 - 1.0;
      }
      normalizeArr(mB+(idx*mM), mM);
   }
   for (int idx = 0; idx < mN; idx++) {
      *getPI(idx) = getRandVal(mN);
   }
   normalizeArr(mPI, mN);
} 

void HMM::forwardPass(int* obserArr, int T)
{
   //compute a0[i]
   *getC(0) = 0;
   for (int idx = 0; idx < mN; idx++) {
      float _a = (*getPI(idx)) * (*getB(idx, obserArr[0])); 
      *getAlpha(0, idx) = _a;
      *getC(0) = (*getC(0)) + _a;
   }

   //scale the a0(i)
   if (*getC(0) != 0) *getC(0) = 1.0 / (*getC(0));
   for (int idx = 0; idx < mN; idx++) {
      *getAlpha(0, idx) = (*getAlpha(0, idx)) * (*getC(0));
   }

   //compute at(i)
   for (int t = 1; t < T; t++) {
      *getC(t) = 0;
      for (int idx = 0; idx < mN; idx++) {
         *getAlpha(t, idx) = 0;
         for (int jdx = 0; jdx < mN; jdx++) {
            *getAlpha(t, idx) = (*getAlpha(t, idx)) +  ((*getAlpha(t-1, jdx)) * (*getA(jdx, idx)));
         }
         *getAlpha(t, idx) = (*getAlpha(t, idx)) * (*getB(idx, obserArr[t]));
         *getC(t) = (*getC(t)) + (*getAlpha(t, idx));
      }

      //scale at(i)
      if (*getC(t) != 0) *getC(t) = 1.0 / (*getC(t));
      for (int idx = 0; idx < mN; idx++) {
         *getAlpha(t, idx) = (*getAlpha(t, idx)) * (*getC(t));
      }
   }
}

void HMM::backwardPass(int* obserArr, int T)
{
   //let beta_t-1(i) = 1 scaled by cT-1
   for (int idx = 0; idx < mN; idx++) {
      *getBeta(T-1, idx) = *getC(T-1);
   }

   //beta-pass
   for (int t = T-2; t > 0; t--) {
      for (int idx = 0; idx < mN; idx++) {
         *getBeta(t, idx) = 0;
         for (int jdx = 0; jdx <mN; jdx++) {
            *getBeta(t, idx) += (*getA(idx, jdx) * (*getB(jdx, obserArr[t+1])) * (*getBeta(t+1, jdx)));
         }

         //scale beta_ti with same scale factor as a_ti
         *getBeta(t, idx) = (*getBeta(t, idx)) * (*getC(t));
      }
   }
}

void HMM::calcGammaDigamma(int* obserArr, int T)
{
   for (int t = 0; t < T-1; t++) {
      for (int idx = 0; idx < mN; idx++) {
         *getGamma(t, idx) = 0;
         for (int jdx = 0; jdx < mN; jdx++) {
            //No need to normalize since using scaled alpha and beta 
            *getDiGamma(t, idx, jdx) = (*getAlpha(t, idx)) * (*getA(idx, jdx)) * (*getB(jdx, obserArr[t+1])) * (*getBeta(t+1, jdx));
            *getGamma(t, idx) = (*getGamma(t, idx)) + (*getDiGamma(t, idx, jdx));
         }
      }
   }

   //special case for gamma_t-1(i)
   //No need to normalize since using scaled alpha and beta 
   for (int idx = 0; idx < mN; idx++) *getGamma(T-1, idx) = *getAlpha(T-1, idx);
  
}

void HMM::reEstimateModel(int* obserArr, int T)
{
   //re-estimate PI
   for (int idx = 0; idx < mN; idx++) *getPI(idx) = *getGamma(0, idx);

#ifndef GRAD_DESCENT

#ifndef USE_FIXED_DIGRAPH
   //re-estimate A
   for (int idx = 0; idx < mN; idx++) {
      for (int jdx = 0; jdx < mN; jdx++) {
         float numer = 0;
         float denom = 0;
         for (int t = 0; t < T-1; t++) {
            numer += *getDiGamma(t, idx, jdx);
            denom += *getGamma(t, idx);
         }
         if (numer == 0) *getA(idx, jdx) = 0;
         else *getA(idx, jdx) = numer / denom;
      }
   }
#endif

   //re-estimate B
   for (int idx = 0; idx < mN; idx++) {
      for (int jdx = 0; jdx < mM; jdx++) {
         float numer = 0;
         float denom = 0;
         for (int t = 0; t < T; t++) {
            if (obserArr[t] == jdx) numer += *getGamma(t, idx);
            denom += *getGamma(t, idx);
         }
         if (numer == 0) *getB(idx, jdx) = 0;
         else *getB(idx, jdx) = numer / denom;
      }
   }

#else

   float _C = 0;
   for (int t = 0; t < T; t++) {
      _C += log(*getC(t));
   }
   float aOverC = LEARNING_RATE / _C; 

   //update weights
   for (int idx = 0; idx < mN; idx++) {
      for (int jdx = 0; jdx < mN; jdx++) {
         float _Aij = 0;
         for (int t = 0; t < T-1; t++) {
            _Aij += *getDiGamma(t,idx,jdx);
         }
         float _Ai = 0;
         for (int t = 0; t < T-1; t++) {
            _Ai += *getGamma(t,idx);
         }
         *getW(idx, jdx) += aOverC*(_Aij - (_Ai*(*getA(idx, jdx))));
      }
   }

   for (int idx = 0; idx < mN; idx++) {
      for (int jdx = 0; jdx < mM; jdx++) {
         float _Bij = 0;
         for (int t = 0; t < T; t++) {
            if (obserArr[t] == jdx) _Bij += *getGamma(t,idx);
         }
         float _Bi = 0;
         for (int t = 0; t < T; t++) {
            _Bi += *getGamma(t,idx);
         }
         *getV(idx, jdx) += aOverC*(_Bij - (_Bi*(*getB(idx, jdx))));
      }
   }

   //re-estimate A
   for (int idx = 0; idx < mN; idx++) {
      float s = 0.0;
      for (int jdx = 0; jdx < mN; jdx++) {
         s += exp(TEMP*(*getW(idx,jdx)));
      }
      for (int jdx = 0; jdx < mN; jdx++) {
         *getA(idx,jdx) = exp(TEMP*(*getW(idx,jdx))) / s;
      }
   }

   //re-estimate B
   for (int idx = 0; idx < mN; idx++) {
      float s = 0.0;
      for (int jdx = 0; jdx < mM; jdx++) {
         s += exp(TEMP*(*getV(idx,jdx)));
      }
      for (int jdx = 0; jdx < mM; jdx++) {
         *getB(idx,jdx) = exp(TEMP*(*getV(idx,jdx))) / s;
      }
   }

#endif
}


float* HMM::getA(int i, int j)
{
#ifndef USE_FIXED_DIGRAPH
   return mA + (i*mN) + j;
#else
   return &DigraphAMat[i][j];
#endif
}
float* HMM::getB(int i, int j)
{
   return mB + (i*mM) + j;
}
float* HMM::getPI(int i)
{
   return mPI + i; 
}

float* HMM::getC(int t)
{
   return mC + t; 
}
float* HMM::getAlpha(int t, int i)
{
   return mAlpha + (t*mN) + i; 
}
float* HMM::getBeta(int t, int i)
{
   return mBeta + (t*mN) + i;
}
float* HMM::getGamma(int t, int i)
{
   return mGamma + (t*mN) + i;
}
float* HMM::getDiGamma(int t, int i, int j)
{
   return mDiGamma + (t*mN*mN) + (i*mN) + j;
}

float* HMM::getW(int i, int j)
{
   return mW + (i*mN) + j;
}
float* HMM::getV(int i, int j)
{
   return mV + (i*mM) + j;
}

//predict the simple shift key assume 
//HHM is trained with: A is fixed digraph matrix, N = M = 26
static int predictMapping(HMM* hmm) {
   //this is the group truth key to be compared
   //e.g., gtKey[0] = 4, then 'a'(0) maps to 'e'(4)
   static const int gtKey[26] = {4, 9, 21, 6, 25, 23, 13, 8, 1, 7, 15, 22, 18, 3, 17, 16, 0, 20, 12, 5, 2, 11, 14, 24, 10, 19};

   int cor = 0;
   for (int i = 0; i < 26; i++) {
      float maxP = 0.0;
      int maxJ = -1;
      for (int j = 0; j < 26; j++) {
         if (*hmm->getB(j, i) >= maxP) {
            maxP = *hmm->getB(j, i);
            maxJ = j;
         }
      }
      if (gtKey[maxJ] == i) cor++;
   }
   printf("cor = %d\n", cor);
   return cor;
}

static int obsers[2615] = {0, 1, 2, 3, 4, 5, 6, 7, 6, 4, 4, 4, 8, 5, 6, 6, 6, 6, 0, 3, 9, 8, 6, 10, 11, 8, 6, 2, 3, 12, 4, 8, 12, 4, 0, 3, 6, 6, 4, 4, 4, 4, 3, 5, 8, 6, 12, 13, 10, 11, 14, 15, 11, 16, 5, 2, 5, 6, 8, 5, 12, 3, 6, 8, 3, 6, 7, 5, 6, 8, 5, 6, 8, 6, 8, 5, 6, 6, 8, 6, 10, 11, 6, 13, 1, 11, 15, 6, 5, 12, 17, 0, 6, 7, 5, 6, 4, 6, 6, 8, 3, 3, 12, 13, 18, 5, 6, 13, 8, 19, 6, 8, 19, 12, 10, 5, 6, 5, 6, 13, 8, 1, 3, 6, 12, 10, 5, 6, 6, 13, 9, 3, 12, 5, 6, 13, 0, 18, 8, 5, 6, 0, 2, 6, 8, 5, 6, 5, 3, 12, 8, 5, 6, 4, 9, 18, 10, 5, 12, 8, 5, 6, 12, 4, 3, 4, 1, 10, 11, 5, 6, 8, 5, 3, 6, 8, 19, 6, 8, 5, 6, 2, 19, 6, 8, 1, 4, 0, 11, 5, 6, 8, 5, 6, 8, 6, 6, 15, 11, 8, 5, 3, 6, 3, 6, 6, 15, 11, 8, 5, 6, 9, 3, 12, 8, 5, 6, 0, 11, 8, 10, 11, 0, 8, 3, 4, 20, 8, 5, 6, 12, 8, 5, 6, 6, 8, 9, 12, 8, 1, 2, 0, 3, 6, 1, 2, 16, 3, 8, 9, 3, 6, 8, 5, 6, 8, 6, 2, 5, 21, 3, 6, 8, 5, 10, 11, 6, 2, 1, 5, 21, 3, 6, 1, 2, 0, 22, 8, 9, 19, 12, 20, 8, 5, 6, 5, 23, 6, 8, 1, 2, 8, 24, 3, 4, 6, 15, 11, 18, 8, 6, 7, 25, 5, 12, 4, 4, 18, 15, 11, 19, 12, 4, 15, 0, 11, 1, 19, 6, 8, 1, 15, 11, 10, 11, 20, 7, 11, 19, 6, 8, 12, 8, 19, 6, 5, 2, 5, 3, 6, 8, 6, 10, 19, 9, 8, 22, 12, 8, 5, 3, 12, 4, 4, 18, 8, 6, 6, 15, 11, 0, 3, 10, 11, 0, 16, 3, 8, 5, 6, 4, 5, 6, 9, 5, 3, 6, 8, 5, 6, 8, 0, 11, 1, 10, 11, 20, 24, 1, 4, 11, 1, 1, 15, 11, 1, 11, 13, 0, 11, 5, 6, 6, 5, 6, 13, 18, 20, 0, 5, 6, 13, 0, 9, 8, 5, 3, 6, 24, 6, 13, 9, 24, 6, 13, 5, 3, 6, 8, 19, 6, 1, 13, 12, 8, 5, 3, 6, 0, 9, 19, 6, 1, 13, 20, 8, 5, 3, 6, 0, 5, 6, 8, 0, 9, 20, 0, 0, 8, 19, 12, 11, 24, 3, 4, 1, 8, 5, 6, 6, 13, 0, 11, 5, 6, 8, 5, 9, 8, 9, 12, 7, 9, 6, 8, 18, 8, 5, 3, 6, 6, 13, 0, 0, 0, 0, 8, 0, 10, 11, 6, 10, 19, 6, 5, 6, 26, 13, 5, 6, 8, 19, 6, 13, 18, 13, 5, 3, 8, 0, 0, 18, 6, 13, 8, 5, 6, 6, 9, 5, 6, 8, 5, 6, 6, 24, 1, 13, 9, 8, 24, 6, 13, 5, 6, 20, 5, 3, 6, 13, 10, 9, 8, 13, 19, 6, 10, 1, 7, 19, 6, 8, 5, 4, 5, 6, 13, 9, 8, 10, 24, 6, 15, 11, 7, 11, 19, 12, 8, 5, 6, 1, 13, 0, 0, 6, 5, 7, 13, 5, 8, 9, 1, 13, 5, 0, 3, 6, 6, 15, 11, 5, 12, 8, 5, 6, 13, 8, 6, 2, 18, 8, 3, 12, 7, 12, 26, 4, 13, 13, 6, 5, 3, 6, 6, 6, 10, 5, 6, 8, 19, 6, 8, 1, 4, 8, 5, 6, 8, 5, 6, 8, 3, 8, 1, 4, 1, 8, 5, 6, 7, 9, 1, 15, 11, 5, 3, 7, 3, 6, 8, 5, 6, 8, 5, 6, 8, 6, 8, 10, 12, 8, 24, 18, 10, 5, 6, 8, 5, 6, 15, 11, 0, 8, 5, 6, 8, 5, 3, 6, 8, 5, 3, 5, 6, 13, 10, 11, 13, 11, 1, 8, 8, 1, 13, 5, 6, 6, 14, 13, 5, 6, 10, 11, 5, 6, 12, 6, 13, 0, 3, 10, 11, 8, 6, 13, 0, 11, 3, 6, 6, 6, 4, 5, 6, 8, 5, 6, 6, 8, 8, 6, 6, 7, 6, 6, 3, 6, 10, 11, 5, 0, 2, 5, 6, 18, 6, 8, 19, 6, 6, 4, 5, 3, 6, 26, 13, 8, 5, 12, 8, 5, 3, 3, 6, 5, 2, 5, 6, 9, 5, 6, 15, 11, 18, 1, 3, 6, 8, 1, 13, 18, 5, 6, 0, 0, 8, 9, 6, 12, 8, 19, 12, 9, 26, 15, 11, 5, 23, 4, 5, 6, 12, 15, 11, 0, 18, 19, 12, 7, 13, 14, 0, 9, 8, 1, 10, 11, 8, 8, 3, 6, 12, 4, 3, 12, 4, 4, 3, 15, 11, 20, 5, 6, 6, 5, 6, 0, 18, 20, 5, 6, 6, 0, 11, 20, 5, 12, 8, 1, 4, 9, 20, 0, 8, 1, 15, 11, 5, 3, 6, 8, 1, 4, 5, 3, 6, 1, 4, 11, 5, 6, 8, 5, 6, 0, 15, 1, 11, 5, 3, 6, 8, 19, 3, 6, 3, 4, 0, 0, 24, 6, 4, 18, 8, 3, 6, 15, 11, 19, 6, 0, 10, 5, 6, 8, 6, 12, 4, 18, 12, 4, 4, 18, 0, 3, 8, 5, 6, 8, 19, 6, 2, 8, 1, 8, 3, 15, 11, 5, 6, 5, 6, 8, 12, 4, 15, 0, 0, 11, 10, 6, 24, 6, 4, 19, 12, 1, 15, 11, 8, 3, 12, 12, 8, 6, 5, 3, 3, 12, 4, 5, 6, 15, 0, 11, 1, 8, 6, 4, 18, 0, 3, 8, 1, 4, 4, 8, 5, 6, 13, 20, 0, 24, 6, 4, 19, 6, 5, 6, 8, 5, 6, 3, 4, 0, 3, 12, 15, 0, 11, 1, 26, 19, 6, 2, 8, 24, 6, 4, 8, 8, 0, 18, 4, 18, 5, 12, 8, 1, 3, 10, 26, 5, 6, 4, 8, 19, 12, 4, 4, 3, 6, 12, 5, 1, 2, 2, 12, 8, 6, 6, 18, 8, 19, 12, 0, 3, 0, 3, 19, 6, 12, 4, 18, 18, 8, 5, 6, 6, 12, 8, 5, 6, 13, 8, 6, 8, 27, 1, 13, 18, 8, 8, 5, 6, 0, 8, 1, 15, 11, 5, 6, 6, 4, 18, 10, 11, 8, 8, 1, 4, 24, 6, 13, 9, 5, 6, 20, 6, 13, 9, 3, 12, 8, 5, 6, 10, 11, 5, 8, 6, 8, 8, 6, 15, 11, 12, 13, 5, 12, 5, 3, 6, 10, 11, 10, 11, 1, 3, 6, 4, 9, 5, 6, 2, 3, 8, 6, 6, 13, 8, 5, 6, 1, 13, 9, 6, 12, 10, 11, 5, 6, 8, 19, 9, 6, 12, 5, 12, 0, 13, 8, 12, 8, 1, 1, 13, 10, 5, 6, 14, 13, 0, 12, 8, 9, 8, 12, 0, 0, 5, 12, 13, 8, 8, 6, 0, 9, 8, 3, 10, 3, 3, 12, 13, 5, 6, 8, 6, 8, 6, 13, 5, 6, 6, 13, 9, 20, 5, 6, 10, 5, 6, 24, 5, 6, 6, 13, 20, 27, 8, 1, 13, 1, 8, 18, 8, 3, 13, 6, 9, 3, 7, 3, 8, 5, 3, 10, 11, 6, 13, 28, 14, 13, 5, 6, 26, 13, 9, 8, 9, 5, 6, 5, 12, 13, 6, 13, 8, 5, 6, 8, 6, 13, 1, 11, 13, 8, 5, 6, 5, 6, 5, 6, 0, 0, 10, 11, 18, 0, 15, 11, 8, 6, 6, 4, 6, 1, 8, 1, 4, 10, 11, 19, 3, 18, 8, 19, 6, 8, 1, 4, 11, 6, 9, 10, 11, 8, 5, 6, 5, 6, 6, 13, 6, 13, 1, 4, 10, 11, 12, 8, 19, 12, 4, 27, 6, 8, 6, 6, 6, 7, 6, 8, 3, 6, 6, 5, 3, 12, 8, 6, 8, 3, 0, 13, 5, 6, 20, 15, 0, 11, 6, 17, 15, 11, 8, 5, 6, 8, 5, 6, 5, 6, 6, 2, 5, 3, 18, 6, 15, 11, 18, 1, 12, 7, 1, 15, 11, 3, 0, 10, 11, 1, 0, 10, 11, 0, 10, 1, 8, 3, 15, 11, 19, 6, 10, 1, 5, 3, 6, 8, 1, 2, 25, 5, 12, 15, 11, 18, 8, 5, 3, 6, 8, 5, 12, 13, 6, 18, 6, 15, 11, 8, 0, 6, 5, 6, 2, 20, 8, 27, 6, 10, 5, 3, 8, 19, 12, 26, 1, 4, 0, 11, 2, 8, 5, 6, 6, 2, 8, 5, 6, 7, 8, 1, 2, 9, 18, 8, 19, 6, 8, 3, 6, 6, 4, 1, 4, 0, 11, 5, 22, 10, 11, 5, 27, 8, 0, 9, 5, 12, 9, 8, 5, 6, 1, 17, 4, 10, 11, 6, 5, 12, 8, 5, 6, 15, 11, 18, 10, 3, 12, 4, 18, 8, 5, 6, 1, 15, 11, 0, 3, 8, 1, 4, 10, 11, 1, 11, 3, 10, 11, 5, 6, 6, 13, 20, 8, 6, 7, 11, 15, 11, 19, 6, 10, 11, 8, 6, 4, 5, 6, 2, 5, 6, 6, 8, 19, 3, 6, 13, 17, 6, 13, 10, 11, 19, 6, 8, 12, 4, 4, 1, 5, 3, 6, 5, 27, 6, 6, 6, 8, 1, 2, 5, 6, 11, 1, 11, 15, 0, 11, 20, 8, 6, 8, 8, 5, 6, 8, 1, 3, 11, 1, 11, 4, 9, 1, 0, 3, 10, 11, 1, 8, 6, 6, 4, 3, 6, 15, 11, 6, 0, 7, 11, 19, 3, 0, 3, 6, 6, 4, 9, 8, 5, 6, 5, 12, 4, 3, 8, 5, 6, 8, 1, 2, 0, 3, 10, 11, 8, 5, 6, 6, 2, 3, 6, 10, 11, 1, 13, 0, 0, 7, 8, 3, 4, 0, 0, 0, 8, 6, 27, 6, 15, 11, 0, 5, 6, 8, 19, 6, 18, 5, 6, 8, 12, 15, 0, 11, 8, 6, 8, 3, 22, 8, 5, 6, 4, 1, 18, 5, 3, 6, 6, 13, 1, 19, 6, 2, 3, 4, 0, 3, 8, 10, 24, 3, 6, 1, 4, 8, 19, 6, 0, 2, 6, 1, 4, 0, 11, 8, 6, 13, 5, 6, 26, 13, 20, 8, 3, 6, 8, 5, 6, 8, 5, 6, 6, 0, 8, 6, 13, 8, 9, 6, 12, 8, 27, 1, 0, 11, 4, 10, 11, 8, 8, 6, 2, 6, 7, 14, 2, 22, 6, 8, 9, 5, 6, 8, 5, 6, 8, 5, 6, 15, 11, 0, 6, 4, 18, 3, 12, 10, 6, 1, 15, 11, 18, 5, 6, 22, 8, 5, 19, 6, 6, 13, 5, 6, 6, 13, 18, 20, 8, 5, 6, 1, 13, 5, 6, 0, 5, 3, 6, 2, 18, 20, 8, 5, 6, 8, 3, 6, 6, 6, 11, 8, 5, 6, 13, 11, 20, 8, 6, 12, 4, 1, 4, 18, 9, 10, 11, 20, 26, 4, 18, 12, 4, 1, 4, 12, 24, 6, 4, 19, 6, 8, 1, 4, 11, 1, 10, 11, 5, 6, 1, 15, 11, 27, 12, 4, 6, 8, 5, 6, 6, 8, 25, 5, 12, 0, 15, 11, 10, 11, 5, 3, 6, 12, 9, 8, 6, 6, 0, 2, 5, 12, 8, 6, 3, 6, 6, 12, 4, 0, 0, 1, 15, 11, 1, 20, 0, 8, 18, 13, 5, 6, 8, 12, 9, 19, 6, 6, 5, 3, 12, 8, 12, 4, 1, 5, 2, 5, 3, 6, 6, 4, 18, 0, 3, 8, 5, 12, 8, 3, 3, 6, 6, 1, 4, 0, 18, 8, 19, 12, 8, 1, 10, 11, 5, 3, 6, 6, 12, 4, 18, 10, 11, 1, 8, 1, 13, 0, 11, 8, 9, 5, 3, 6, 12, 7, 0, 6, 2, 20, 8, 5, 6, 8, 3, 13, 1, 8, 5, 6, 6, 4, 5, 6, 9, 8, 5, 3, 6, 5, 6, 18, 8, 5, 6, 15, 11, 1, 24, 5, 6, 2, 18, 1, 4, 8, 3, 6, 10, 11, 1, 20, 3, 4, 0, 3, 8, 1, 12, 15, 0, 11, 5, 3, 12, 8, 0, 0, 4, 5, 3, 6, 9, 8, 5, 6, 7, 19, 6, 8, 6, 13, 5, 0, 3, 6, 8, 5, 6, 12, 27, 9, 5, 3, 12, 0, 8, 13, 8, 19, 6, 19, 6, 24, 6, 13, 1, 9, 8, 1, 15, 0, 11, 5, 3, 6, 6, 12, 24, 8, 9, 5, 3, 6, 12, 7, 5, 6, 8, 6, 12, 8, 1, 15, 11, 20, 8, 1, 4, 0, 11, 5, 6, 8, 12, 4, 15, 8, 6, 8, 6, 0, 6, 5, 8, 19, 12, 8, 6, 4, 9, 8, 1, 8, 7, 5, 3, 15, 11, 20, 3, 12, 7, 11, 1, 11, 6, 7, 6, 12, 15, 11, 6, 12, 18, 8, 19, 12, 0, 13, 12, 15, 11, 18, 8, 12, 4, 3, 6, 8, 1, 4, 18, 0, 11, 15, 11, 10, 19, 12, 8, 6, 7, 11, 15, 0, 8, 1, 12, 15, 11, 8, 19, 12, 7, 6, 8, 5, 6, 0, 11, 15, 11, 1, 20, 8, 3, 6, 10, 11, 1, 20, 12, 4, 15, 11, 1, 3, 7, 11, 1, 11, 8, 9, 7, 5, 6, 12, 4, 15, 11, 1, 11, 8, 5, 3, 6, 6, 8, 3, 12, 4, 3, 15, 11, 3, 6, 9, 5, 21, 3, 8, 6, 10, 19, 12, 8, 5, 6, 1, 15, 11, 8, 5, 6, 15, 11, 18, 3, 13, 5, 3, 6, 3, 13, 5, 3, 6, 8, 6, 12, 26, 15, 0, 11, 18, 26, 15, 0, 11, 18, 14, 2, 5, 3, 12, 26, 4, 8, 6, 5, 12, 26, 4, 18, 12, 7, 9, 12, 5, 12, 26, 4, 20, 8, 12, 7, 6, 1, 8, 25, 12, 26, 4, 9, 12, 4, 12, 8, 5, 7, 5, 3, 12, 26, 8, 3, 4, 5, 26, 4, 8, 6, 8, 1, 11, 18, 2, 5, 6, 6, 7, 5, 12, 8, 19, 6, 7, 5, 6, 6, 6, 13, 1, 8, 5, 6, 5, 12, 26, 4, 6, 7, 6, 8, 19, 6, 1, 15, 0, 11, 18, 7, 5, 6, 26, 2, 8, 3, 6, 8, 12, 7, 5, 7, 5, 6, 7, 19, 3, 7, 5, 6, 8, 5, 12, 26, 4, 8, 5, 6, 26, 2, 6, 5, 7, 5, 0, 0, 5, 6, 26, 0, 13, 3, 6, 6, 1, 15, 11, 18, 3, 3, 1, 13, 11, 18, 7, 8, 3, 6, 17, 2, 0, 3, 5, 3, 6, 3, 13, 1, 8, 5, 6, 5, 3, 12, 3, 12, 7, 12, 8, 3, 6, 8, 6, 8, 1, 11, 18, 7, 9, 6, 3, 8, 6, 6, 7, 8, 6, 0, 0, 7, 11, 3, 6, 6, 7, 6, 7, 1, 4, 26, 7, 5, 6, 8, 9, 20, 5, 12, 4, 0, 4, 20, 10, 1, 7, 1, 0, 3, 6, 26, 1, 4, 8, 5, 6, 8, 6, 8, 1, 11, 18, 5, 6, 6, 6, 12, 2, 12, 8, 5, 12, 4, 11, 1, 7, 3, 13, 10, 11, 1, 5, 6, 2, 5, 22, 8, 6, 19, 0, 27, 3, 6, 5, 8, 1, 13, 1, 13, 3, 14, 4, 12, 6, 6, 6, 12, 4, 9, 8, 8, 1, 3, 3, 6, 26, 2, 5, 6, 6, 0, 8, 6, 8, 6, 8, 6, 8, 6, 1, 4, 18, 0, 1, 2};
static const int M = 29;
static const int T = 2615;

void dumpScores(HMM* hmm, std::string label, int* obsers, int total, int t, std::string dumpFile) //score consecutive t observations from the array
{
   std::fstream fs;
   fs.open (dumpFile, std::fstream::out | std::fstream::app);
   for (int k = 0; k + t <= total; k++) {
      float logScore = hmm->getScore(obsers+k, t);
      fs << label << "," << logScore << "\n";
   }
   fs.close();
}

int main(int argc, const char** argv) {
   if (argc != 4) {
      printf("Usage: %s <N> <minIters> <epsilon>\n", argv[0]);
      return -1;
   }
   const int N = std::stoi(argv[1]);
   const int minIters = std::stoi(argv[2]);
   const float epsilon = std::stof(argv[3]);


   //start training
   HMM* hmm = new HMM(N, M, minIters, epsilon);
   if (!hmm) {
      printf("no memory\n");
      return -3;
   }

   hmm->fit(obsers, T);

   //clean up
   delete hmm;

   return 0;
}



