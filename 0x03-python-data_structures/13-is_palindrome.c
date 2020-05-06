#include "lists.h"
/**
 * is_palindrome - determine if a list is palindrome
 * @head: pointer to the first node
 * Return: 1 if is palindrome otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head, *temp2 = NULL, *head2 = NULL;

	if (*head == NULL)
		return (1);
	while (temp != NULL)
	{
		new_f(&head2, temp->n);
		temp = temp->next;
	}
	temp = *head;
	temp2 = head2;
	while (temp != NULL)
	{
		if (temp->n == temp2->n)
		{
			temp = temp->next;
			temp2 = temp2->next;
		}
		else
			break;
	}
	free_listint(head2);
	if (temp == NULL)
		return (1);
	return (0);
}
/**
 * new_f - add node to a linked list at the beginning
 * @head: address passed by reference
 * @n: value for the new node
 * Return: new node
 */
listint_t *new_f(listint_t **head, int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}
