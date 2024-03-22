#include "lists.h"

/**
 * free_dlistint - frees a db list
 * @head: ptr to head
 * Return: void
 */

void free_dlistint(dlistint_t *head)
{
	dlistint_t *next_node = NULL, *trav = head;

	while (trav != NULL)
	{
		next_node = trav->next;
		free(trav);
		trav = next_node;
	}
}