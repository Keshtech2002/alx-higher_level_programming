#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: sorted singly linked list
 * @number: number to insert
 * Return: NULL if it failed, address of new node added
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;
	
	if (number)
	{
		new = malloc(sizeof(listint_t));
		new -> n = number;
	}
	if (*head == NULL || new == NULL)
		return (NULL);
	temp = *head;
	while (temp -> next != NULL)
	{
		if ((new -> n) < (temp -> n))
		{
			new -> next = temp -> next;
			temp -> next = new;
			break;
		}
		temp = temp -> next;
	}
	return (new);
}
