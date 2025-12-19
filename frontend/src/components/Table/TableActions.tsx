import {
  EyeIcon,
  PencilSquareIcon,
  TrashIcon,
} from "@heroicons/react/24/outline"

export type TableActionsProps = {
  onView?: () => void
  onEdit?: () => void
  onDelete?: () => void
}

export default function TableActions({
  onView,
  onEdit,
  onDelete,
}: TableActionsProps) {
  return (
    <div className="flex justify-center gap-2">
      {onView && (
        <button
          className="btn btn-ghost btn-sm"
          onClick={onView}
          title="View"
        >
          <EyeIcon className="w-5 h-5" />
        </button>
      )}

      {onEdit && (
        <button
          className="btn btn-ghost btn-sm"
          onClick={onEdit}
          title="Edit"
        >
          <PencilSquareIcon className="w-5 h-5" />
        </button>
      )}

      {onDelete && (
        <button
          className="btn btn-ghost btn-sm text-error"
          onClick={onDelete}
          title="Delete"
        >
          <TrashIcon className="w-5 h-5" />
        </button>
      )}
    </div>
  )
}
