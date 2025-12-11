
import Layout from "../layouts/Layout";
import { useParams } from "react-router-dom";

export default function EditTicket() {
  const { id } = useParams();

  return (
    <Layout>
      <h2>Edit Ticket</h2>
      <p>You are Editing the ticket whit ID: {id}</p>

      <form>
        <div style={{ marginBottom: "12px" }}>
          <input
            type="text"
            defaultValue={`Title of the Ticket #${id}`}
            style={{ width: "100%", padding: "8px" }}
          />
        </div>

        <div style={{ marginBottom: "12px" }}>
          <textarea
            defaultValue={`Description of the Ticket #${id}`}
            style={{ width: "100%", padding: "8px", minHeight: "120px" }}
          />
        </div>

        <button type="button" style={{ padding: "8px 16px" }}>
          Save changes
        </button>
      </form>
    </Layout>
  );
}
