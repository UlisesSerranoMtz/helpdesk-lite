import { useTickets } from "@/hooks/useTickets"
import { useRef } from "react"
import Navbar from "@/components/Navbar"
import { Outlet } from "react-router-dom"
import TicketModalForm from "@/components/Tickets/TicketModalForm"

export default function Layout() {
  const ticketsHook = useTickets()
  const modalRef = useRef(null)

  const openCreate = () => modalRef.current.openForCreate()
  const openEdit = (ticket) => modalRef.current.openForEdit(ticket)

  return (
    <>
      <Navbar onCreateTicket={openCreate} />

      <main className="p-6">
        <Outlet
          context={{
            ...ticketsHook,
            openEditTicket: openEdit,
          }}
        />
      </main>

      <TicketModalForm
        ref={modalRef}
        onSuccess={ticketsHook.fetchTickets}
      />
    </>
  )
}
