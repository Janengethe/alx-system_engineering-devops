#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - create infinite sleep loop
 * Return: 0
 */
int infinite_while(void)
{
while (1)
{
sleep(1);
}
return (0);
}

/**
 * main - create 5 zombie processes
 * Return: infinite_while zombies
 */
int main(void)
{
pid_t zombiepid;
unsigned int i;

/*for 5 processes*/
for (i = 0; i < 5; i++)
{
zombiepid = fork();/*create zombie processed*/
if (zombiepid == 0)
exit(0);/*kill child*/
else/*still running yet dead*/
printf("Zombie process created, PID: %d\n", zombiepid);
}
return (infinite_while());
}
