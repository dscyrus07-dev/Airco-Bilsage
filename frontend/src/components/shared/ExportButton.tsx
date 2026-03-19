import { Button } from "@/components/ui/button";
import { Download } from "lucide-react";
import { toast } from "sonner";

export function ExportButton({ label = "Export CSV" }: { label?: string }) {
  return (
    <Button
      variant="outline"
      size="sm"
      className="h-8 text-xs"
      onClick={() => toast.success("Export started", { description: "Your file will download shortly." })}
    >
      <Download className="h-3.5 w-3.5 mr-1.5" />
      {label}
    </Button>
  );
}
