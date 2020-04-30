#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - insert a node with a specific value
 * @head: pointer head of that linked list
 * @number: value to insert in the list
 * Return: the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nw, *cur, *p;

	if (!head)
	{
		return (NULL);
	}
	nw = malloc(sizeof(listint_t))
	if (!nw)
	{
		return (NULL);
	}
	nw->n = number;
	nw->next = NULL;
	p = NULL;
	cur = *head;

	while (cur && cur->n < number)
	{
		p = cur;
		cur = cur->next;
	}
	new->next = cur;
	if (p)
		p->next = nw;
	else
		*head = nw;
	return (nw);
}
