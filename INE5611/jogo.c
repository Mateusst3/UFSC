#include <stdio.h>
#include <stdlib.h>
#include <ncurses.h>
#include <time.h>
#include <stdlib.h>
#include <pthread.h>

int x;
struct timespec ts = {0, 40000000L};

// Fun��o gotoxy
void gotoxy(int x, int y)
{
	printf("\033[%d;%df", y, x);
	fflush(stdout);
}

void bomba_horizontal(int x, int y)
{
	gotoxy(x, y);
	printf("<");
	gotoxy(x + 1, y);
	printf("___");
}
void apaga_bomba_horizontal(int x, int y)
{
	gotoxy(x, y);
	printf(" ");
	gotoxy(x + 1, y);
	printf("   ");
}
void bomba(int x, int y)
{
	gotoxy(x, y);
	printf("/\\");
	gotoxy(x, y + 1);
	printf("||");
	gotoxy(x - 1, y + 2);
	printf("/||\\");
}
void apaga_bomba(int x, int y)
{
	gotoxy(x, y);
	printf("  ");
	gotoxy(x, y + 1);
	printf("  ");
	gotoxy(x - 1, y + 2);
	printf("    ");
}
void explode_bomba(int x, int y)
{
	gotoxy(x, y);
	printf("*");
	nanosleep(&ts, NULL);
	printf(" ");
	gotoxy(x, y - 1);
	printf("O");
	gotoxy(x - 1, y);
	printf("O O");
	gotoxy(x, y + 1);
	printf("O");
	nanosleep(&ts, NULL);
	gotoxy(x, y - 1);
	printf(" ");
	gotoxy(x - 1, y);
	printf("   ");
	gotoxy(x, y + 1);
	printf(" ");

	gotoxy(x, y - 2);
	printf("o");
	gotoxy(x - 2, y);
	printf("o   o");
	gotoxy(x, y + 2);
	printf("o");
	nanosleep(&ts, NULL);
	gotoxy(x, y - 2);
	printf(" ");
	gotoxy(x - 2, y);
	printf("     ");
	gotoxy(x, y + 2);
	printf(" ");
}
void nave(int x, int y)
{
	gotoxy(x, y);
	printf("/");
	gotoxy(x + 1, y - 1);
	printf("___");
	gotoxy(x + 4, y);
	printf("\\");
	gotoxy(x, y + 1);
	printf("v-V-v");
	gotoxy(x, y + 1);
	printf("V-v-V");
}
void apaga_nave(int x, int y)
{
	gotoxy(x, y);
	printf(" ");
	gotoxy(x + 1, y - 1);
	printf("   ");
	gotoxy(x + 4, y);
	printf(" ");
	gotoxy(x, y + 1);
	printf("     ");
	gotoxy(x, y + 1);
	printf("     ");
}
void canhao(int x, int y)
{
	gotoxy(x, y);
	printf("+-+");
	gotoxy(x, y + 1);
	printf("| |");
	gotoxy(x, y + 2);
	printf("| |");
	gotoxy(x, y + 3);
	printf("+-+");
}
void *ThreadFuncNave(void *linha);

void *ThreadFuncNave(void *linha)
{
	int n;
	n = (int)linha;
	for (int x = 79; x >= 0; x--)
	{
		nave(x, linha);
		nanosleep(&ts, NULL);
		apaga_nave(x, linha);
	}
}

void *ThreadFuncBomba(void *arg);
void *ThreadFuncBomba(void *arg)
{
	for (int y = 20; y >= 5; y--)
	{
		bomba(40, y);
		nanosleep(&ts, NULL);
		apaga_bomba(40, y);
	}
	return NULL;
}

int main()
{
	char montanhas[] = {10, 17, 14, 18, 16, 19, 12, 18, 13, 24, 10, 17, 14, 18, 16, 19, 12, 18, 13, 24, 10, 17, 14, 18, 16, 19, 12, 18, 13, 24, 10, 17, 14, 18, 16, 19, 12, 18, 13, 24};
	int coluna = 5;
	int linha = 3;
	int k = 0;
	system("cls");
	for (int i = 0; i < 18;)
	{
		// printf("aqui");
		for (int j = montanhas[i]; j <= montanhas[i + 1]; j++)
		{
			gotoxy(k, j); // printf("%i %i\n", k, j);//
			printf("\\");
			k++;
		}

		for (int j = montanhas[i]; j >= montanhas[i + 1]; j--)
		{
			gotoxy(k, j); // printf("%i %i\n", k, j);//
			printf("/");
			k++;
		}
		i++;
	}
	// Providing a seed value
	srand(time(NULL));
	k = 21;

	canhao(40, 23);
	bomba_horizontal(43, 26);
	bomba_horizontal(43, 25);
	bomba_horizontal(43, 24);
	bomba_horizontal(43, 23);
	bomba_horizontal(43, 22);
	bomba_horizontal(43, 21);
	// while (5)
	// {
	// 	linha = 2 + (rand() % 5);
	// 	pthread_t idThread;
	// 	pthread_create(&idThread, NULL, ThreadFuncNave, linha);
	// 	pthread_join(idThread, NULL);
	// 	// for (int x = 79; x >= 0; x--)
	// 	// {
	// 	// 	nave(x, linha);
	// 	// 	nanosleep(&ts, NULL);
	// 	// 	apaga_nave(x, linha);
	// 	// }
	// 	apaga_bomba_horizontal(43, k);
	// 	for (int y = 20; y >= 5; y--)
	// 	{
	// 		bomba(40, y);
	// 		nanosleep(&ts, NULL);
	// 		apaga_bomba(40, y);
	// 	}
	// 	explode_bomba(40, 7);
	// 	k++;
	// 	if (k == 26)
	// 	{
	// 		bomba_horizontal(43, 26);
	// 	}
	// }
	while (5)
	{
		linha = 2 + (rand() % 5);
		int linha2 = 1 + (rand() % 5);
		int linha3 = 3 + (rand() % 5);
		pthread_t idThreadNave, idThreadBomba;
		pthread_create(&idThreadNave, NULL, ThreadFuncNave, (void *)linha);
		pthread_create(&idThreadNave, NULL, ThreadFuncNave, (void *)linha2);
		pthread_create(&idThreadNave, NULL, ThreadFuncNave, (void *)linha3);

		pthread_create(&idThreadBomba, NULL, ThreadFuncBomba, NULL);
		pthread_join(idThreadNave, NULL);
		pthread_join(idThreadBomba, NULL);
		apaga_bomba_horizontal(43, k);
		explode_bomba(40, 7);
		k++;
		if (k == 26)
		{
			bomba_horizontal(43, 26);
		}
	}
	getch();
}
