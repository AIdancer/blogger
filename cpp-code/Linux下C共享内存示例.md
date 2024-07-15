### 使用linux系统调用实现共享内存
```c++
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <unistd.h>

#define SHM_SIZE 1024

const char* initial_value = "Hello, shared memory.";

void write_to_shared_memory(key_t key, int shm_id) {
    char *shm_addr;
    shm_addr = (char *)shmat(shm_id, NULL, 0);
    if (shm_addr == (char *)(-1)) {
        perror("shmat failed");
        exit(1);
    }
    printf("Writing to shared memory...\n");
    strcpy(shm_addr, initial_value);
    printf("Written : %s\n", shm_addr);
    shmdt(shm_addr);
}

void read_from_shared_memory(key_t key, int shm_id) {
    char *shm_addr;
    shm_addr = (char *)shmat(shm_id, NULL, 0);
    if (shm_addr == (char *)(-1)) {
        perror("shmat failed");
        exit(1);
    }
    printf("Reading from shared memory...\n");
    printf("Read: %s\n", shm_addr);

    shmdt(shm_addr);
}

int main() {
    key_t key = ftok("./shmfile", 'a');
    if (key == -1) {
        perror("ftok failed");
        exit(1);
    }
    int shm_id = shmget(key, SHM_SIZE, IPC_CREAT | 0666);
    if (shm_id == -1) {
        perror("shmget failed");
        exit(1);
    }
    pid_t pid = fork();
    if (pid == -1) {
        perror("fork failed");
        exit(1);
    } else if (pid == 0) {
        write_to_shared_memory(key, shm_id);
    } else {
        wait(NULL);
        read_from_shared_memory(key, shm_id);
    }
    return 0;
}
```
