import { useRef } from "react"
import { useOutletContext } from "react-router-dom"
import TableActions from "@/components/Table/TableActions"
import DeleteModal from "@/components/Tickets/DeleteModal"
import { STATUS_LABEL, PRIORITY_LABEL } from "@/components/Tickets/constants/ticketLabels"

export default function TableList() {
  const {
    tickets,
    loading,
    error,
    filters,
    setFilters,
    removeTicket,
    openEditTicket,
  } = useOutletContext()

  const deleteModalRef = useRef(null)

  if (loading) {
    return (
      <div className="fixed inset-0 flex items-center justify-center bg-base-100/70 z-50">
        <span className="loading loading-spinner loading-xl"></span>
      </div>
    )
  }  

  return (
    <>
      <div className="flex gap-4 mb-4">
        <select
          className="select select-bordered"
          value={filters.status}
          onChange={(e) =>
            setFilters({ ...filters, status: e.target.value })
          }
        >
          <option value="">All status</option>
          <option value="open">Open</option>
          <option value="in_progress">In progress</option>
          <option value="closed">Closed</option>
        </select>

        <select
          className="select select-bordered"
          value={filters.priority}
          onChange={(e) =>
            setFilters({ ...filters, priority: e.target.value })
          }
        >
          <option value="">All priority</option>
          <option value="low">Low</option>
          <option value="medium">Medium</option>
          <option value="high">High</option>
        </select>
      </div>

      <table className="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Status</th>
            <th>Priority</th>
            <th className="text-center">Actions</th>
          </tr>
        </thead>

        <tbody>
          {tickets.map((ticket) => (
            <tr key={ticket.id} className="hover:bg-base-300">
              <td>{ticket.id}</td>

              <td>
                <div className="font-semibold">{ticket.title}</div>
                <div className="text-sm opacity-70">
                  {ticket.description}
                </div>
              </td>

              <td>
                <span className="badge badge-outline">
                  {STATUS_LABEL[ticket.status]}
                </span>
              </td>

              <td>
                <span
                  className={`badge ${
                    ticket.priority === "high"
                      ? "badge-error"
                      : ticket.priority === "medium"
                      ? "badge-warning"
                      : "badge-success"
                  }`}
                >
                  {PRIORITY_LABEL[ticket.priority]}
                </span>
              </td>

              <td className="text-center">
                <TableActions
                  onEdit={() => openEditTicket(ticket)}
                  onDelete={() => deleteModalRef.current.open(ticket.id)}
                />
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      <DeleteModal
        ref={deleteModalRef}
        onConfirm={removeTicket}
      />
    </>
  )
}
