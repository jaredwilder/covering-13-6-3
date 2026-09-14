#include <bits/stdc++.h>
using namespace std;
struct Cov { uint64_t lo,hi; };
inline Cov OR(Cov a,Cov b){return {a.lo|b.lo,a.hi|b.hi};}
inline Cov ANDNOT(Cov a,Cov b){return {a.lo&~b.lo,a.hi&~b.hi};}
inline bool zero(Cov a){return !(a.lo|a.hi);} 
struct B330 { uint64_t w[6]; };
inline B330 band(B330 a,const B330&b){for(int i=0;i<6;i++)a.w[i]&=b.w[i];return a;}
inline int bcount(const B330&a){int s=0;for(int i=0;i<6;i++)s+=__builtin_popcountll(a.w[i]);return s;}
inline bool bzero(const B330&a){for(auto x:a.w)if(x)return false;return true;}
inline void clearbit(B330& a,int i){a.w[i>>6]&=~(1ULL<<(i&63));}
inline bool testbit(const B330&a,int i){return (a.w[i>>6]>>(i&63))&1ULL;}
inline int firstbit(const B330&a){for(int w=0;w<6;w++)if(a.w[w])return w*64+__builtin_ctzll(a.w[w]);return -1;}
int pid[12][12], pa[66],pb[66]; vector<array<int,4>> Qs; Cov cm[330]; B330 covm[66]; Cov ALL;
struct Star { array<uint16_t,5> e; bool operator<(Star const&o)const{return e<o.e;} bool operator==(Star const&o)const{return e==o.e;} };
long long localnodes;

vector<Star> enumerateLocal(const vector<array<int,4>>&H,int y){
 vector<int> others;int loc[12];fill(loc,loc+12,-1);for(int z=0;z<12;z++)if(z!=y){loc[z]=others.size();others.push_back(z);} 
 Cov covered{0,0};
 for(int c:H[y]){
  vector<int>A;for(int z=0;z<12;z++)if(z!=y && find(H[z].begin(),H[z].end(),c)!=H[z].end())A.push_back(loc[z]);
  if(A.size()!=5){cerr<<"bad residual block size\n";exit(2);}for(int i=0;i<5;i++)for(int j=i+1;j<5;j++){int p=pid[A[i]][A[j]];if(p<64)covered.lo|=1ULL<<p;else covered.hi|=1ULL<<(p-64);}
 }
 Cov need=ANDNOT(ALL,covered);
 B330 avail{};for(int i=0;i<330;i++)avail.w[i>>6]|=1ULL<<(i&63);
 vector<array<int,5>> sols; array<int,5> chosen{};
 function<void(int,Cov,B330)> rec=[&](int d,Cov cv,B330 av){
  localnodes++;
  Cov un=ANDNOT(need,cv); int rem=5-d;
  if(zero(un)){
   if(rem==0){sols.push_back(chosen);return;}
   vector<int> inds;for(int i=0;i<330;i++)if(testbit(av,i))inds.push_back(i);
   function<void(int,int)> extra=[&](int st,int r){if(r==0){sols.push_back(chosen);return;}for(int q=st;q<=(int)inds.size()-r;q++){chosen[5-r]=inds[q];extra(q+1,r-1);}};
   extra(0,rem);return;
  }
  if(rem==0)return;
  int rootu=0,pairu=0;uint64_t x=un.lo;while(x){int b=__builtin_ctzll(x); if(pa[b]==11||pb[b]==11)rootu++;else pairu++;x&=x-1;}x=un.hi;while(x){int bb=__builtin_ctzll(x)+64;if(pa[bb]==11||pb[bb]==11)rootu++;else pairu++;x&=x-1;}
  if((rootu+3)/4>rem || (pairu+5)/6>rem)return;
  B330 best{};int bestn=999;
  auto consider=[&](int b){B330 o=band(av,covm[b]);int n=bcount(o);if(n==0){bestn=0;best=o;return false;}if(n<bestn){bestn=n;best=o;}return true;};
  x=un.lo;while(x){int b=__builtin_ctzll(x);if(!consider(b))return;x&=x-1;}x=un.hi;while(x){int b=__builtin_ctzll(x)+64;if(!consider(b))return;x&=x-1;}
  B330 work=av, opts=best;
  while(!bzero(opts)){
   int i=firstbit(opts); clearbit(opts,i); clearbit(work,i); chosen[d]=i; rec(d+1,OR(cv,cm[i]),work);
  }
 };
 rec(0,covered,avail);
 sort(sols.begin(),sols.end());sols.erase(unique(sols.begin(),sols.end()),sols.end());
 vector<Star> out;out.reserve(sols.size());
 for(auto sol:sols){Star s;for(int t=0;t<5;t++){uint16_t bm=1u<<y;for(int u:Qs[sol[t]])bm|=1u<<others[u];s.e[t]=bm;}sort(s.e.begin(),s.e.end());out.push_back(s);}sort(out.begin(),out.end());out.erase(unique(out.begin(),out.end()),out.end());return out;
}
bool paircomp(int y,const Star&a,int z,const Star&b){
 array<uint16_t,5>x{},w{};int nx=0,nw=0;for(auto e:a.e)if((e>>z)&1)x[nx++]=e;for(auto e:b.e)if((e>>y)&1)w[nw++]=e;if(nx!=nw)return false;sort(x.begin(),x.begin()+nx);sort(w.begin(),w.begin()+nw);for(int i=0;i<nx;i++)if(x[i]!=w[i])return false;return true;
}
int main(){
 int q=0;for(int i=0;i<12;i++)for(int j=i+1;j<12;j++){pid[i][j]=pid[j][i]=q;pa[q]=i;pb[q]=j;q++;}ALL={~0ULL,3ULL};
 for(int a=0;a<11;a++)for(int b=a+1;b<11;b++)for(int c=b+1;c<11;c++)for(int d=c+1;d<11;d++)Qs.push_back({a,b,c,d});
 for(int i=0;i<330;i++){Cov m{0,0};for(int u:Qs[i]){int p=pid[u][11];if(p<64)m.lo|=1ULL<<p;else m.hi|=1ULL<<(p-64);}for(int a=0;a<4;a++)for(int b=a+1;b<4;b++){int p=pid[Qs[i][a]][Qs[i][b]];if(p<64)m.lo|=1ULL<<p;else m.hi|=1ULL<<(p-64);}cm[i]=m;for(int b=0;b<66;b++){bool on=b<64?((m.lo>>b)&1):((m.hi>>(b-64))&1);if(on)covm[b].w[i>>6]|=1ULL<<(i&63);}}
 vector<array<int,4>> allsets;for(int a=0;a<8;a++)for(int b=a+1;b<8;b++)for(int c=b+1;c<8;c++)for(int d=c+1;d<8;d++)allsets.push_back({a,b,c,d});
 ifstream f("residual_orbits.txt");int n;f>>n;ofstream out("direct_court.tsv");out<<"orbit\tglue\ty\tz\tdy\tdz\tlocalnodes\n";
 int surv=0;auto T0=chrono::steady_clock::now();
 for(int o=1;o<=n;o++){
  vector<array<int,4>> H(12);for(int t=0;t<12;t++){int idx;f>>idx;H[t]=allsets[idx];}
  localnodes=0;vector<vector<Star>> D(12);bool badlocal=false;for(int y=0;y<12;y++){D[y]=enumerateLocal(H,y);if(D[y].empty()){cerr<<"orbit "<<o<<" zero local "<<y<<"\n";out<<o<<"\t0\t"<<y<<"\t-1\t0\t0\t"<<localnodes<<"\n";badlocal=true;break;}}
  if(badlocal)continue;
  bool dead=false;int ky=-1,kz=-1;
  for(int y=0;y<12&&!dead;y++)for(int z=y+1;z<12&&!dead;z++){long long c=0;for(auto &a:D[y])for(auto &b:D[z])if(paircomp(y,a,z,b))c++;if(c==0){dead=true;ky=y;kz=z;}}
  if(dead){cerr<<"orbit "<<o<<" DEAD pair "<<ky<<","<<kz<<" dom "<<D[ky].size()<<","<<D[kz].size()<<" nodes "<<localnodes<<"\n";out<<o<<"\t0\t"<<ky<<"\t"<<kz<<"\t"<<D[ky].size()<<"\t"<<D[kz].size()<<"\t"<<localnodes<<"\n";}
  else {surv++;cerr<<"orbit "<<o<<" PAIR-SURVIVES domains";for(auto&d:D)cerr<<" "<<d.size();cerr<<" nodes "<<localnodes<<"\n";out<<o<<"\t1\t-1\t-1\t0\t0\t"<<localnodes<<"\n";}
 }
 double sec=chrono::duration<double>(chrono::steady_clock::now()-T0).count();cerr<<"DONE survivors="<<surv<<" sec="<<sec<<"\n";
}
