#include <bits/stdc++.h>
using namespace std;
struct Key { uint64_t lo; uint64_t hi; bool operator==(Key const&o)const{return lo==o.lo&&hi==o.hi;} bool operator<(Key const&o)const{return hi<o.hi||(hi==o.hi&&lo<o.lo);} };
struct KH { size_t operator()(Key const&k)const {return k.lo*0x9e3779b97f4a7c15ULL ^ (k.hi+0x9e3779b97f4a7c15ULL+(k.lo<<6)+(k.lo>>2));}};
int A; vector<array<unsigned char,16>> allowp;
uint64_t sup[16][13][5];
array<uint8_t,70> sbits; array<array<uint8_t,70>,70> pmaskm;
int action[1152][70], G=0;
int sel[12], depth=0, degc[8];
unsigned char cnt[12][16]; uint64_t poss[12][5];
long long nodes=0, leaves=0; unordered_set<Key,KH> seen; vector<Key> reps;
inline bool emptyP(uint64_t *p){return !(p[0]|p[1]|p[2]|p[3]|p[4]);}
inline void andeq(uint64_t *p,const uint64_t*q){for(int w=0;w<5;w++)p[w]&=q[w];}
Key keyFromSelTrans(int g){Key k{0,0};for(int t=0;t<depth;t++){int j=action[g][sel[t]]; if(j<64)k.lo|=1ULL<<j;else k.hi|=1ULL<<(j-64);}return k;}
Key canonical(){Key best{~0ULL,~0ULL};for(int g=0;g<G;g++){Key k=keyFromSelTrans(g);if(k<best)best=k;}return best;}
void dfs(int nxt){
 nodes++;
 int need=12-depth;
 if(depth==12){for(int v=0;v<8;v++)if(degc[v]!=6)return; leaves++; Key k=canonical(); if(seen.insert(k).second){reps.push_back(k); if(reps.size()<=30||reps.size()%100==0)cerr<<"orbit "<<reps.size()<<" leaves "<<leaves<<" nodes "<<nodes<<"\n";} return;}
 if(70-nxt<need)return;
 int deficit=0;for(int v=0;v<8;v++){if(degc[v]>6)return;deficit+=6-degc[v];} if(deficit!=4*need)return;
 for(int v=0;v<8;v++)if(degc[v]<6){int av=0;for(int j=nxt;j<70;j++) if((sbits[j]>>v)&1) av++; if(degc[v]+av<6)return;}
 for(int j=nxt;j<70;j++){
  uint8_t bj=sbits[j]; bool bad=false;for(int v=0;v<8;v++)if(((bj>>v)&1)&&degc[v]>=6){bad=true;break;}if(bad)continue;
  uint64_t oldposs[12][5]; unsigned char oldc[12]; int oldm[12];
  bool ok=true; int upd=0;
  for(int t=0;t<depth;t++){
   for(int w=0;w<5;w++)oldposs[t][w]=poss[t][w];
   int m=pmaskm[sel[t]][j]; oldm[t]=m; oldc[t]=cnt[t][m]; int nc=++cnt[t][m]; upd=t+1; andeq(poss[t],sup[m][nc]); if(emptyP(poss[t])){ok=false;break;}
  }
  if(!ok){for(int t=0;t<upd;t++){int m=oldm[t]; cnt[t][m]=oldc[t];for(int w=0;w<5;w++)poss[t][w]=oldposs[t][w];} continue;}
  memset(cnt[depth],0,16); for(int t=0;t<depth;t++)cnt[depth][pmaskm[j][sel[t]]]++;
  for(int w=0;w<5;w++)poss[depth][w]=0;
  for(int a=0;a<A;a++)poss[depth][a>>6]|=1ULL<<(a&63);
  for(int m=0;m<16;m++)if(cnt[depth][m])andeq(poss[depth],sup[m][cnt[depth][m]]);
  if(!emptyP(poss[depth])){
   sel[depth]=j;for(int v=0;v<8;v++)if((bj>>v)&1)degc[v]++;depth++;dfs(j+1);depth--;for(int v=0;v<8;v++)if((bj>>v)&1)degc[v]--;
  }
  for(int t=0;t<depth;t++){int m=oldm[t];cnt[t][m]=oldc[t];for(int w=0;w<5;w++)poss[t][w]=oldposs[t][w];}
 }
}
int main(){
 ifstream f("patA_allowed_patterns.txt");f>>A;allowp.resize(A);for(int a=0;a<A;a++)for(int m=0;m<16;m++){int x;f>>x;allowp[a][m]=x;}
 memset(sup,0,sizeof(sup));for(int m=0;m<16;m++)for(int c=0;c<=12;c++)for(int a=0;a<A;a++)if(allowp[a][m]>=c)sup[m][c][a>>6]|=1ULL<<(a&63);
 vector<array<int,4>> sets;for(int a=0;a<8;a++)for(int b=a+1;b<8;b++)for(int c=b+1;c<8;c++)for(int d=c+1;d<8;d++)sets.push_back({a,b,c,d});
 map<array<int,4>,int> idx;for(int i=0;i<70;i++){idx[sets[i]]=i;uint8_t b=0;for(int v:sets[i])b|=1<<v;sbits[i]=b;}
 for(int i=0;i<70;i++){int pos[8];fill(pos,pos+8,-1);for(int k=0;k<4;k++)pos[sets[i][k]]=k;for(int j=0;j<70;j++){int m=0;for(int v:sets[j])if(pos[v]>=0)m|=1<<pos[v];pmaskm[i][j]=m;}}
 array<int,4> p1={0,1,2,3}; do{array<int,4> p2={4,5,6,7};do{int mp[8];for(int i=0;i<4;i++){mp[i]=p1[i];mp[i+4]=p2[i];}for(int j=0;j<70;j++){array<int,4>T;for(int k=0;k<4;k++)T[k]=mp[sets[j][k]];sort(T.begin(),T.end());action[G][j]=idx[T];}G++;}while(next_permutation(p2.begin(),p2.end()));}while(next_permutation(p1.begin(),p1.end()));
 cerr<<"A="<<A<<" G="<<G<<"\n";
 int first=idx[{0,1,2,3}];sel[0]=first;depth=1;memset(degc,0,sizeof(degc));for(int v:sets[first])degc[v]++;
 memset(cnt,0,sizeof(cnt));for(int w=0;w<5;w++)poss[0][w]=0;for(int a=0;a<A;a++)poss[0][a>>6]|=1ULL<<(a&63);
 auto st=chrono::steady_clock::now();dfs(first+1);double sec=chrono::duration<double>(chrono::steady_clock::now()-st).count();
 cerr<<"DONE nodes="<<nodes<<" leaves="<<leaves<<" orbits="<<reps.size()<<" sec="<<sec<<"\n";
 ofstream o("residual_orbits.txt");o<<reps.size()<<"\n";for(auto k:reps){vector<int> H;for(int i=0;i<70;i++){bool on=i<64?((k.lo>>i)&1):((k.hi>>(i-64))&1);if(on)H.push_back(i);}for(int i=0;i<(int)H.size();i++){if(i)o<<' ';o<<H[i];}o<<"\n";}
}
