import { forwardRef, useImperativeHandle, useRef, useState } from "react"
import { createTicket, updateTicket } from "@/components/Tickets/api/tickets.js"

const INITIAL_FORM = {
  title: "",
  description: "",
  priority: "medium",
}

const TicketModalForm = forwardRef(function TicketModalForm(
  { onSuccess },
  ref
) {
  const dialogRef = useRef(null)

  const [form, setForm] = useState(INITIAL_FORM)
  const [mode, setMode] = useState("create")
  const [ticketId, setTicketId] = useState(null)

  const [error, setError] = useState(null)
  const [loading, setLoading] = useState(false)

  const resetForm = () => {
    setForm(INITIAL_FORM)
    setMode("create")
    setTicketId(null)
    setError(null)
    setLoading(false)
  }

  useImperativeHandle(ref, () => ({
    openForCreate: () => {
      resetForm()
      dialogRef.current?.showModal()
    },

    openForEdit: (ticket) => {
      setForm({
        title: ticket.title ?? "",
        description: ticket.description ?? "",
        priority: ticket.priority ?? "medium",
      })
      setMode("edit")
      setTicketId(ticket.id)
      dialogRef.current?.showModal()
    },

    close: () => {
      dialogRef.current?.close()
      resetForm()
    },
  }))

  const handleChange = (e) => {
    const { name, value } = e.target
    setForm((prev) => ({ ...prev, [name]: value }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError(null)

    if (!form.title.trim()) {
      setError("Title is required")
      return
    }

    try {
      setLoading(true)

      if (mode === "create") {
        await createTicket(form)
      } else {
        await updateTicket(ticketId, form)
      }

      onSuccess?.()
      dialogRef.current.close()
      resetForm()
    } catch (err) {
      setError(err.message || "Unexpected error")
    } finally {
      setLoading(false)
    }
  }

  return (
    <dialog
      ref={dialogRef}
      className="modal modal-bottom sm:modal-middle"
      onClose={resetForm}
    >
      <div className="modal-box">
        <h3 className="font-bold text-lg mb-4">
          {mode === "create" ? "Create Ticket" : "Edit Ticket"}
        </h3>

        {error && (
          <div className="alert alert-error mb-4">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          <input
            name="title"
            placeholder="Title"
            className="input input-bordered w-full"
            value={form.title}
            onChange={handleChange}
          />

          <textarea
            name="description"
            placeholder="Description"
            className="textarea textarea-bordered w-full"
            value={form.description}
            onChange={handleChange}
          />

          <select
            name="priority"
            className="select select-bordered w-full"
            value={form.priority}
            onChange={handleChange}
          >
            <option value="low">Low</option>
            <option value="medium">Medium</option>
            <option value="high">High</option>
          </select>

          <div className="modal-action">
            <button
              type="button"
              className="btn btn-ghost"
              onClick={() => {
                dialogRef.current.close()
                resetForm()
              }}
            >
              Cancel
            </button>

            <button className="btn btn-primary" disabled={loading}>
              {loading
                ? "Saving..."
                : mode === "create"
                ? "Create"
                : "Update"}
            </button>
          </div>
        </form>
      </div>
    </dialog>
  )
})

export default TicketModalForm
