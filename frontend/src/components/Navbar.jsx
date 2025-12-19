export default function Navbar({ onCreateTicket }) {
    return (
      <div className="navbar bg-base-100 shadow-sm">
        <div className="navbar-start">
          <a className="btn btn-ghost text-xl">HelpDesk</a>
        </div>
  
        <div className="navbar-center hidden lg:flex">
          <input
            type="text"
            placeholder="Search"
            className="input input-bordered w-48 md:w-auto"
          />
        </div>
  
        <div className="navbar-end">
          <button className="btn btn-primary" onClick={onCreateTicket}>
            Create Ticket
          </button>
        </div>
      </div>
    )
  }
  