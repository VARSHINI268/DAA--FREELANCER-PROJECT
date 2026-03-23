const { spawn } = require("child_process");

const input = {
    skills: ["web", "js"],
    budget: 400,
    deadline: 3
};

const python = spawn("python", ["backend.py"]);

python.stdin.write(JSON.stringify(input));
python.stdin.end();

python.stdout.on("data", (data) => {
    try {
        const result = JSON.parse(data.toString());

        if (result.status === "success") {
            console.log("✅ Assigned to:", result.freelancer);
        } else if (result.status === "fail") {
            console.log("❌ No suitable freelancer found");
        } else {
            console.log("⚠️ Error:", result.error);
        }
    } catch (err) {
        console.log("Parsing error:", err);
    }
});

python.stderr.on("data", (data) => {
    console.error("Python Error:", data.toString());
});