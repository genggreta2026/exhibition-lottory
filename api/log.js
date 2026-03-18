import fs from 'fs';
import path from 'path';

export default function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).end();
  }

  const { name, phone, email, prize } = req.body;

  const logText = `
================================
时间：${new Date().toLocaleString()}
姓名：${name}
手机：${phone}
邮箱：${email}
奖品：${prize}
================================
`;

  const logPath = path.join(process.cwd(), 'log.txt');
  fs.appendFileSync(logPath, logText, 'utf8');

  res.status(200).json({ ok: true });
}
