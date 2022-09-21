//https://codeforces.com/blog/entry/76149
using namespace std;
template<int D, typename T>
struct Vec : public vector<Vec<D - 1, T> > {
  static_assert(D >= 1, "Vector dimension must be greater than zero!");
  template<typename... Args>
  Vec(int n = 0, Args... args) : vector<Vec<D - 1, T>>(n, Vec<D - 1, T>(args...)) {
  }
};
//Vec<3, int> x(12, 12, 12,1.0); 3 dim vector each containg 12 arrays, filled with the number 1
template<typename T>
struct Vec<1, T> : public vector<T> {
  Vec(int n = 0, const T& val = T()) : vector<T>(n, val) {
  }
};
