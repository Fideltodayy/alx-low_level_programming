#include "lists.h"

/**
 * dlistint_len - get number of nodes in a list
 * @h: head ptr
 * Return: number of nodes
 */

size_t dlistint_len(const dlistint_t *h)
{
	size_t nodes_num = 0;
	const dlistint_t *trav = h;

	while (trav != NULL)
	{
		nodes_num++;
		trav = trav->next;
	}
	return (nodes_num);
}