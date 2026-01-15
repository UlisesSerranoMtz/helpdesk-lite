import { useEffect, useState } from "react"
import { getTickets, deleteTicket } from "@/components/Tickets/api/tickets"

export function useTickets() {
  const [tickets, setTickets] = useState([])
  const [listLoading, setlistLoading] = useState(true)
  const [deleteLoading, setdeleteLoading] = useState(true)
  const [error, setError] = useState(null)

  const [filters, setFilters] = useState({
    status: "",
    priority: "",
    search: "",
  })
  const fetchTickets = async (customFilters = filters) => {
    try {
      setlistLoading(true)
      setError(null)
      const data = await getTickets(customFilters)
      setTickets(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setlistLoading(false)
    }
  }

  const removeTicket = async (id) => {
    try{
      setdeleteLoading(true)
      await deleteTicket(id)
      await fetchTickets()
    }catch (err){
      setError(err.message)
    }finally{
      setdeleteLoading(false)
    }
  }

  useEffect(() => {
    fetchTickets()
  }, [filters])

  return {
    tickets,
    listLoading,
    deleteLoading,
    error,
    filters,
    setFilters,
    fetchTickets,
    removeTicket,
  }
}
