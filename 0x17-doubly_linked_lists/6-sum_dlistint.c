#include "lists.h"

/**
 * sum_dlistint - sum of data in a db list
 * @head: head ptr
 * Return: sum
 */

int sum_dlistint(dlistint_t *head)
{
	int sum = 0;
	dlistint_t *trav = head;

	while (trav)
	{
		sum += trav->n;
		trav = trav->next;
	}
	return (sum);
}