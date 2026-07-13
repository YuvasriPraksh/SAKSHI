import { Routes, Route } from "react-router-dom";

import Landing from "./pages/Landing";
import Login from "./pages/Login";
import OfficerDashboard from "./pages/OfficerDashboard";
import CreateCase from "./pages/CreateCase";
import CaseDetails from "./pages/CaseDetails";
import Timeline from "./pages/Timeline";
import AuditTrail from "./pages/AuditTrail";
import Alerts from "./pages/Alerts";
import ComplianceDashboard from "./pages/ComplianceDashboard";
import PublicGuide from "./pages/PublicGuide";
import NotFound from "./pages/NotFound";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/login" element={<Login />} />
      <Route path="/dashboard" element={<OfficerDashboard />} />
      <Route path="/create-case" element={<CreateCase />} />
      <Route path="/case/:id" element={<CaseDetails />} />
      <Route path="/timeline" element={<Timeline />} />
      <Route path="/audit" element={<AuditTrail />} />
      <Route path="/alerts" element={<Alerts />} />
      <Route path="/compliance" element={<ComplianceDashboard />} />
      <Route path="/guide" element={<PublicGuide />} />
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
}

export default App;