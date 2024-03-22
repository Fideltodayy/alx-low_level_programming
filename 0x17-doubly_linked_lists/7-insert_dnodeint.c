#include "lists.h"

/**
 * insert_dnodeint_at_index - insert node at nth index
 * @h: double head ptr
 * @idx: index
 * @n: data of new node
 * Return: new node address
 */

dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	unsigned int counter = 0;
	dlistint_t *current = *h, *new_node = malloc(sizeof(dlistint_t));

	if (new_node == NULL)
		return (NULL);

	while (current)
	{
		/*insert at beginning*/
		if (idx == 0)
		{
			new_node->n = n;
			new_node->prev = NULL;
			new_node->next = current;
			current->prev = new_node;
			*h = new_node;
			return (*h);
		}
		if (counter == idx)
		{
			/*if last node*/
			if (current->next == NULL)
			{
				new_node->prev = current;
				current->next = new_node;
				new_node->next = NULL;
				new_node->n = n;
				return (new_node);
			}
			new_node->prev = current->prev;
			new_node->n = n;
			new_node->next = current;
			current->prev->next = new_node;
			current->prev = new_node;
			return (*h);
		}
		counter++;
		current = current->next;
	}
	return (NULL);
}
