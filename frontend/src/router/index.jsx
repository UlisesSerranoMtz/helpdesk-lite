import { createBrowserRouter } from "react-router-dom";
import TicketList from "../pages/TicketList";
import NewTicket from "../pages/NewTicket";
import EditTicket from "../pages/EditTicket";

export const router = createBrowserRouter([
  { path: "/tickets", element: <TicketList /> },
  { path: "/tickets/new", element: <NewTicket /> },
  { path: "/tickets/edit/:id", element: <EditTicket /> },
]);
