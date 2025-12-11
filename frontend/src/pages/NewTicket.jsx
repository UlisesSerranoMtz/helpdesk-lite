
import Layout from "../layouts/Layout";

export default function NewTicket() {
  return (
    <Layout>
      <h2>Crear Ticket</h2>

      <form>
        <div style={{ marginBottom: "12px" }}>
          <input
            type="text"
            placeholder="Título del ticket"
            style={{ width: "100%", padding: "8px" }}
          />
        </div>

        <div style={{ marginBottom: "12px" }}>
          <textarea
            placeholder="Descripción"
            style={{ width: "100%", padding: "8px", minHeight: "120px" }}
          />
        </div>

        <button type="button" style={{ padding: "8px 16px" }}>
          Guardar
        </button>
      </form>
    </Layout>
  );
}
