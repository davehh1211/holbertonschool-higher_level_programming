#include "lists.h"
void reverse_listint(listint_t **head);
size_t listint_len(const listint_t *h);
/**
 * is_palindrome - determines if a list of number is pali
 * @head: the list to evaluate
 * Return: 0 in success, 1 in failure.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int i = 0, len = 0;

	if (head == NULL || (*head)->next == NULL || *head == NULL)
		return (1);
	len = listint_len(*head);
	if (len % 2 != 0)
		len = len / 2;
	else
	{
		len = len / 2;
		len -= 1;
	}
	while (i <= len)
	{
		tmp = tmp->next;
		i++;
	}
	reverse_listint(&tmp);
	while (tmp)
	{
		if ((*head)->n != tmp->n)
			return (0);
		tmp = tmp->next;
		*head = (*head)->next;
	}
	return (1);
}

/**
* listint_len - print the number of ocurrences in printing
* @h: list to print
* Return: print number of iterations
*/
size_t listint_len(const listint_t *h)
{
	int n = 0, i = 0;

	for (i = 0; h != NULL; i++)
	{
		h = h->next;
		n++;
	}
	return (n);
}

/**
 * reverse_listint - reverse a list
 * @head: list to reverse
 * Return: nothing
 */
void reverse_listint(listint_t **head)
{
	listint_t *curr = NULL, *next;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = curr;
		curr = *head;
		*head = next;
	}
	*head = curr;
}
