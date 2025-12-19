import { forwardRef, useImperativeHandle, useRef, useState } from "react"

const DeleteModal = forwardRef(function DeleteModal({ onConfirm }, ref) {
  const dialogRef = useRef(null)
  const [ticketId, setTicketId] = useState(null)

  useImperativeHandle(ref, () => ({
    open: (id) => {
      setTicketId(id)
      dialogRef.current?.showModal()
    },
  }))

  const handleConfirm = async () => {
    if (!ticketId) return
    await onConfirm(ticketId)
    setTicketId(null)
    dialogRef.current?.close()
  }

  return (
    <dialog ref={dialogRef} className="modal modal-bottom sm:modal-middle">
      <div className="modal-box">
        <h3 className="font-bold text-lg">Delete ticket?</h3>
        <p className="py-4">This action cannot be undone.</p>

        <div className="modal-action">
          <button
            className="btn btn-ghost"
            onClick={() => dialogRef.current.close()}
          >
            Cancel
          </button>

          <button
            className="btn btn-error"
            onClick={handleConfirm}
          >
            Delete
          </button>
        </div>
      </div>
    </dialog>
  )
})

export default DeleteModal
