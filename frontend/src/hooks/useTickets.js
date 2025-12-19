import { useEffect, useState } from "react"
import { getTickets, deleteTicket } from "@/components/Tickets/api/tickets"

export function useTickets() {
  const [tickets, setTickets] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  const fetchTickets = async () => {
    try {
      setLoading(true)
      setError(null)
      const data = await getTickets()
      setTickets(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const removeTicket = async (id) => {
    await deleteTicket(id)
    await fetchTickets()
  }

  useEffect(() => {
    fetchTickets()
  }, [])

  return {
    tickets,
    loading,
    error,
    fetchTickets,
    removeTicket,
  }
}
