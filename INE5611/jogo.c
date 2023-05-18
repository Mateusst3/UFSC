#include <stdio.h>
#include <stdlib.h>
#include <curses.h>
#include <time.h>
#include <pthread.h>
#include <string.h>

int x;
int global_x_nave, global_y_nave, global_x_bomba, global_y_bomba;
int global_x_canhao = 40;
int contador = 0;
struct timespec ts = {0, 50000000L};
struct timespec tsNave;
struct timespec tsNaveEasy = {0, 30000000L};
struct timespec tsNaveMedium = {0, 20000000L};
struct timespec tsNaveHard = {0, 10000000L};
pthread_t idThreadNave, idThreadBomba, idCanhao, idContador;
int contador_tempo = 0;
bool respondido = false;

// Função gotoxy
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

void apaga_canhao(int x, int y)
{
	{
		gotoxy(x, y);
		printf("  ");
		gotoxy(x, y + 1);
		printf("   ");
		gotoxy(x, y + 2);
		printf("   ");
		gotoxy(x, y + 3);
		printf("   ");
	}
}

void atualiza_contador()
{
	gotoxy(2, 40);
	char str[5];
	sprintf(str, "%d", contador);
	printf("Abates: %s\n", str);
}

void *ThreadAtualizaContador()
{
	while (5)
	{
		atualiza_contador();
	}
}

void *ThreadFuncNave(void *linha)
{
	int n;
	n = (int)linha;
	for (int x = 79; x >= 0; x--)
	{
		global_x_nave = x;
		global_y_nave = linha;
		nave(x, linha);
		nanosleep(&tsNave, NULL);
		apaga_nave(x, linha);
	}
	return NULL;
}

void *ThreadFuncBomba(void *arg)
{
	while (5)
	{
		int x_canhao = global_x_canhao;
		int x_bomba = global_x_canhao;
		int ch = getch();
		if (ch == ' ')
		{
			for (int y = 20; y >= 0; y--)
			{
				if ((global_x_bomba == global_x_nave && global_x_bomba == global_x_nave))
				{
					explode_bomba(global_x_bomba, global_y_bomba);
					pthread_cancel(idThreadNave);
					contador++;
				}
				else
				{
					bomba(x_bomba, y);
					global_y_bomba = y;
					global_x_bomba = 40;
					nanosleep(&ts, NULL);
					apaga_bomba(x_bomba, y);
				}
			}
		}
		if (ch == 'a')
		{
			x_canhao = x_canhao - 2;
		}
		else if (ch == 'd')
		{
			x_canhao = x_canhao + 2;
		}
		global_x_canhao = x_canhao;
		canhao(x_canhao, 20); // Atualiza a posição do canhão na tela
		nanosleep(&ts, NULL);
		apaga_canhao(x_canhao, 20);
	}

	return NULL;
}

int main()
{
	printf("Qual a dificuldade? facil, medio ou dificil: ");
	int coluna = 5;
	int linha = 3;
	int k = 0;
	// Providing a seed value
	srand(time(NULL));
	// k = 21;

	initscr();			   // Inicializa o modo curses
	cbreak();			   // Desabilita o buffer de linha
	noecho();			   // Desabilita o eco do caractere digitado
	nodelay(stdscr, TRUE); // Torna getch() uma função não bloqueante
	while (!respondido)
	{
		char str[50];
		char str2[50] = "facil";
		char str3[50] = "medio";
		char str4[50] = "dificil";
		int i, i2, i3;
		scanf("%s", &str);
		i = strcmp(str, str2);
		i2 = strcmp(str, str3);
		i3 = strcmp(str, str4);
		if (i == 0)
		{
			tsNave = tsNaveEasy;
			respondido = true;
		}
		else if (i2 == 0)
		{
			tsNave = tsNaveMedium;
			respondido = true;
		}
		else if (i3 == 0)
		{
			tsNave = tsNaveHard;
			respondido = true;
		}
	}

	pthread_create(&idThreadBomba, NULL, ThreadFuncBomba, NULL);
	atualiza_contador();
	while (contador < 20 && contador_tempo <= 80)
	{
		atualiza_contador();
		linha = 2 + (rand() % 5);
		int linha2 = 1 + (rand() % 5);
		int linha3 = 3 + (rand() % 5);
		pthread_create(&idThreadNave, NULL, ThreadFuncNave, (void *)linha);
		pthread_join(idThreadNave, NULL);
		contador_tempo++;
		system("clear");
	}

	if (contador_tempo >= 80 && contador <= 20)
	{
		pthread_cancel(idThreadNave);
		pthread_cancel(idThreadBomba);
		printf("Voce perdeu!");
	}

	if (contador_tempo <= 80 && contador >= 20)
	{
		pthread_cancel(idThreadNave);
		pthread_cancel(idThreadBomba);
		printf("Voce ganhou!");
	}

	return 0;
}
