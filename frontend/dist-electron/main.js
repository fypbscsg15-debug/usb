import { ipcMain as d, shell as i, app as o, BrowserWindow as a } from "electron";
import t from "node:path";
import { fileURLToPath as h } from "node:url";
const l = t.dirname(h(import.meta.url));
d.handle("open-external", async (n, p) => {
  try {
    return await i.openExternal(p), { success: !0 };
  } catch (s) {
    return console.error("Failed to open external link:", s), { success: !1, error: s.message };
  }
});
process.env.DIST = t.join(l, "../dist");
process.env.VITE_PUBLIC = o.isPackaged ? process.env.DIST : t.join(process.env.DIST, "../public");
let e;
const r = process.env.VITE_DEV_SERVER_URL;
function c() {
  e = new a({
    icon: t.join(process.env.VITE_PUBLIC, "electron-vite.svg"),
    webPreferences: {
      preload: t.join(l, "preload.js")
    },
    width: 1200,
    height: 800
  }), e.webContents.setWindowOpenHandler(({ url: n }) => n.startsWith("https:") || n.startsWith("http:") || n.startsWith("mailto:") || n.startsWith("sms:") ? (i.openExternal(n), { action: "deny" }) : { action: "allow" }), e.webContents.on("did-finish-load", () => {
    e == null || e.webContents.send("main-process-message", (/* @__PURE__ */ new Date()).toLocaleString());
  }), r ? e.loadURL(r) : e.loadFile(t.join(process.env.DIST, "index.html"));
}
o.on("window-all-closed", () => {
  process.platform !== "darwin" && (o.quit(), e = null);
});
o.on("activate", () => {
  a.getAllWindows().length === 0 && c();
});
o.whenReady().then(c);
