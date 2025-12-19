import { createBrowserRouter } from "react-router-dom"
import Layout from "@/layouts/Layout"

import TableList from "@/components/Table/TableLIst"

export const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      {
        index: true,
        element: <TableList />,
      },
    ],
  },
])
