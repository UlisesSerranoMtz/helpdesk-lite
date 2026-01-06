import { useEffect, useState } from "react"
import { getTickets, deleteTicket } from "@/components/Tickets/api/tickets"

export function useTickets() {
  const [tickets, setTickets] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  const [filters, setFilters] = useState({
    status: "",
    priority: "",
    search: "",
  })
  const fetchTickets = async (customFilters = filters) => {
    try {
      setLoading(true)
      setError(null)
      const data = await getTickets(customFilters)
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
  }, [filters])

  return {
    tickets,
    loading,
    error,
    filters,
    setFilters,
    fetchTickets,
    removeTicket,
  }
}
