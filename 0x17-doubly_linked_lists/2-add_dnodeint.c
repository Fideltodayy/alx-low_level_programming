#include "lists.h"

/**
 * add_dnodeint - add node at beginning of list
 * @head: double ptr to head
 * @n: data of new node
 * Return: address of head ptr
 */

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new_node = malloc(sizeof(dlistint_t));
	dlistint_t *temp = *head;

	if (new_node == NULL)
		return (NULL);
	/*if no node exists at first*/
	if (temp == NULL)
	{
		new_node->n = n;
		new_node->prev = NULL;
		new_node->next = NULL;
		*head = new_node;
		return (*head);
	}
	else
	{
		new_node->n = n;
		new_node->prev = NULL;
		new_node->next = temp;
		temp->prev = new_node;
		*head = new_node;
		return (*head);
	}
}
