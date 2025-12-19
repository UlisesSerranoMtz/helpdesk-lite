const API_URL = import.meta.env.VITE_API_URL

export async function getTickets() {
  const res = await fetch(`${API_URL}/tickets`)
  if (!res.ok) throw new Error("Error fetching tickets")
  return res.json()
}

export async function createTicket(data) {
  const res = await fetch(`${API_URL}/tickets`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  })

  if (!res.ok) {
    const err = await res.json()
    throw new Error(err.detail || "Error creating ticket")
  }

  return res.json()
}

export async function updateTicket(id, data) {
  const res = await fetch(`${API_URL}/tickets/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  })

  if (!res.ok) {
    const err = await res.json()
    throw new Error(err.detail || "Error updating ticket")
  }

  return res.json()
}

export async function deleteTicket(id) {
  const res = await fetch(`${API_URL}/tickets/${id}`, {
    method: "DELETE",
  })

  if (!res.ok) throw new Error("Error deleting ticket")
}
