#ifndef __HMM_MOD_H__
#define __HMM_MOD_H__
class HMM {
public:
   HMM(int N, int M, int minIters, float epsilon);
   virtual ~HMM();
   float getScore(int* obserArr, int T);
   void fit(int* obserArr, int T);

private:
   void setupTable(int T);
   float getRandVal(int k); //return a random value around 1/k
   void normalizeArr(float* arr, int T);
   void randomInit(); //random init table
   void forwardPass(int* obserArr, int T);
   void backwardPass(int* obserArr, int T);
   void calcGammaDigamma(int* obserArr, int T);
   void reEstimateModel(int* obserArr, int T);
   void freeTables();
   void printModel();

private:
   int mN;
   int mM;
   int mMinIters;
   int mEps;
   float mOldLogProb;

public: //table access
   float* getA(int i, int j);
   float* getB(int i, int j);
   float* getPI(int i);

   float* getW(int i, int j);
   float* getV(int i, int j);
private: //table access
   float* getC(int t);
   float* getAlpha(int t, int i);
   float* getBeta(int t, int i);
   float* getGamma(int t, int i);
   float* getDiGamma(int t, int i, int j);

private: //table
   float* mA;
   float* mB;
   float* mPI;

   float* mC;
   float* mAlpha;
   float* mBeta;
   float* mGamma;
   float* mDiGamma;

   float* mW;
   float* mV;

};

#endif /*__HMM_MOD_H__*/
