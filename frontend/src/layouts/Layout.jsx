export default function Layout({ children }) {
    return (
      <div
        style={{
          minHeight: "100vh",
          background: "#f5f5f5",
          padding: "0",
          margin: "0",
        }}
      >
        <header
          style={{
            padding: "20px",
            background: "#242424",
            color: "#fff",
            fontSize: "28px",
            fontWeight: "bold",
            textAlign: "center",
          }}
        >
          HelpDesk Lite
        </header>
  
        <main
          style={{
            maxWidth: "800px",
            margin: "40px auto",
            background: "#fff",
            padding: "30px",
            borderRadius: "8px",
            boxShadow: "0 2px 10px rgba(0,0,0,0.1)",
          }}
        >
          {children}
        </main>
      </div>
    );
  }
  