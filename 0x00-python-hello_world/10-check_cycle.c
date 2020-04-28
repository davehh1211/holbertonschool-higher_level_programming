#include "lists.h"
/**
 * check_cycle - checks if a linked list has cycles
 * @list: the list to be checked
 * Return: integer
 */
int check_cycle(listint_t *list)
{
	listint_t *tempo, *auxiliar;

	tempo = list, auxiliar = list;
	while (auxiliar != NULL && tempo != NULL && tempo->next != NULL)
	{
		tempo = tempo->next->next;
		auxiliar = auxiliar->next;
		if (tempo == auxiliar)
		{
			return (1);
		}
	}
	return (0);
}
