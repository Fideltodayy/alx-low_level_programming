#include "lists.h"

/**
 * add_dnodeint_end - add node at beginning of list
 * @head: double ptr to head
 * @n: data of new node
 * Return: address of new el
 */

dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
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
	while (temp->next != NULL)
		temp = temp->next;
	new_node->n = n;
	new_node->prev = temp;
	new_node->next = NULL;
	temp->next = new_node;
	return (new_node);
}