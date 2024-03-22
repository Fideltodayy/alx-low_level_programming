#include "lists.h"

/**
 * get_dnodeint_at_index - get nth node of list
 * @index: index passed
 * @head: head ptr
 * Return: relevant address that matches index
 */

dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int counter = 0;
	dlistint_t *trav = head;

	while (trav != NULL)
	{
		if (counter == index)
			return (trav);
		counter++;
		trav = trav->next;
	}
	return (NULL);
}
