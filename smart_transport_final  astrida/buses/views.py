from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bus

@login_required
def bus_list(request):
    """Display a list of available buses."""
    buses = Bus.objects.filter(is_active=True)
    return render(request, 'buses/bus_list.html', {'buses': buses})

@login_required
def bus_details(request, pk):
    """Display details of a specific bus."""
    bus = get_object_or_404(Bus, pk=pk, is_active=True)
    return render(request, 'buses/bus_details.html', {'bus': bus})

'''@login_required
def book_ticket(request, pk):
    """Allow a customer to book a ticket."""
    bus = get_object_or_404(Bus, pk=pk, is_active=True)

    # Simulate ticket booking logic here
    # E.g., Save to a Ticket model (create this model later if needed)

    # Confirmation message
    messages.success(request, f"Your ticket for {bus.name} has been booked!")
    return redirect('buses:bus_list')'''




from .models import Ticket

@login_required
def book_ticket(request, pk):
    bus = get_object_or_404(Bus, pk=pk, is_active=True)

    # Create and save a ticket
    ticket = Ticket.objects.create(customer=request.user, bus=bus)

    messages.success(request, f"Your ticket for {bus.name} has been booked! Ticket ID: {ticket.id}")
    return render(request, 'buses/ticket_confirmation.html', {'ticket': ticket})





@login_required
def ticket_confirmation(request, ticket_id):
    """Display ticket confirmation details."""
    # Get the ticket by its ID
    ticket = get_object_or_404(Ticket, id=ticket_id)

    return render(request, 'ticket_confirmation.html', {'ticket': ticket}) 


