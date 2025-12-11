import Layout from "../layouts/Layout";
import { Link } from "react-router-dom";

export default function TicketList() {
  return (
    <Layout>
      <h2>Tickets list</h2>

      <ul>
        <li>
          Ticket #1 — <Link to="/tickets/edit/1">Edit</Link>
        </li>
        <li>
          Ticket #2 — <Link to="/tickets/edit/2">Edit</Link>
        </li>
        <li>
          Ticket #3 — <Link to="/tickets/edit/3">Edit</Link>
        </li>
      </ul>
    </Layout>
  );
}
