### 条件变量、unique_lock及lock_guard使用
```c++
#include <ctime>

#include <iostream>
#include <thread>
#include <memory>
#include <string>
#include <vector>
#include <mutex>
#include <chrono>
#include <utility>

#include <Windows.h>

using namespace std;

const int N = 10;
mutex mtx;
condition_variable cond;
bool ready[N] = { false };

void consumer(int v) {
    unique_lock<mutex> lock(mtx);
    //cout << "waiting for consume : " << v << endl;
    //cond.wait(lock);
    cond.wait(lock, [&] {return ready[v]; });
    cout << "consuming : " << v << endl;
}

void producer(int v) {
    unique_lock<mutex> lock(mtx);
    cout << "produced : " << v << endl;
    ready[v] = true;
    //cond.notify_one();
    cond.notify_all();
}

int main()
{
    {
        lock_guard<mutex> lock(mtx);
        thread t([] {
            for (int i = 0; i < 10; i++) {
                cout << "sleeping : " << i + 1 << endl;
                this_thread::sleep_for(chrono::seconds(1));
            }
            });
        t.join();
    }

    thread consumers[N];
    for (int i = 0; i < N; i++) {
        consumers[i] = thread(consumer, i);
        consumers[i].detach();
    }

    thread producers[N];
    for (int i = 0; i < N; i++) {
        producers[i] = thread(producer, i);
        producers[i].detach();
    }
    getchar();
    return 0;
}
```
