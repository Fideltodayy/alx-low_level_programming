#include "lists.h"

/**
 * delete_dnodeint_at_index - del node at nth index
 * @head: double head ptr
 * @index: index
 * Return: 1 (success), -1(failed)
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	unsigned int counter = 0;
	dlistint_t *current = *head;

	while (current)
	{
		/*if first node*/
		if (index == 0)
		{
			*head = current->next;
			free(current);
			return (1);
		}
		if (counter == index)
		{
			/*if last node*/
			if (current->next == NULL)
			{
				current->prev->next = NULL;
				free(current);
				return (1);
			}
			current->prev->next = current->next;
			current->next->prev = current->prev;
			free(current);
			return (1);
		}
		counter++;
		current = current->next;
	}
	return (-1);
}
