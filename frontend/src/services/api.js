const BASE='http://localhost:8000/api/v1';
export const api={
 conversations:()=>fetch(`${BASE}/chat/conversations`).then(r=>r.json()),
 newConversation:()=>fetch(`${BASE}/chat/conversations`,{method:'POST'}).then(r=>r.json()),
 conversation:(id)=>fetch(`${BASE}/chat/conversations/${id}`).then(r=>r.json()),
 message:(conversation_id,message)=>fetch(`${BASE}/chat/message`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({conversation_id,message})}).then(r=>r.json())
};
