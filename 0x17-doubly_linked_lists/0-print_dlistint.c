#include "lists.h"

/**
 * print_dlistint - print elements of a list
 * @h: head pointer
 * Return: number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	int nodes_num = 0;
	const dlistint_t *trav = h;

	while (trav != NULL)
	{
		printf("%d\n", trav->n);
		trav = trav->next;
		nodes_num++;
	}
	return (nodes_num);
}