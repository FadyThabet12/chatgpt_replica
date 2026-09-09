import React, {useEffect, useState} from 'react';
import {api} from './services/api';

export default function App(){
 const [chats,setChats]=useState([]),[active,setActive]=useState(null),[messages,setMessages]=useState([]),[input,setInput]=useState(''),[loading,setLoading]=useState(false);
 const refresh=async()=>setChats(await api.conversations());
 useEffect(()=>{refresh()},[]);
 const newChat=async()=>{const x=await api.newConversation(); setActive(x.id); setMessages([]); refresh()};
 const select=async(id)=>{const x=await api.conversation(id);setActive(id);setMessages(x.messages||[])};
 const send=async()=>{if(!input.trim()||!active)return; const text=input;setInput('');setMessages(m=>[...m,{role:'user',content:text}]);setLoading(true);try{const x=await api.message(active,text);setMessages(m=>[...m,{role:'assistant',content:x.answer}]);refresh()}finally{setLoading(false)}};
 return <div className="app"><aside><div className="brand">◉ ChatGPT Replica</div><button className="new" onClick={newChat}>＋ New chat</button><div className="history">{chats.map(c=><button key={c.id} onClick={()=>select(c.id)}>{c.title}</button>)}</div></aside><main><header>ChatGPT Replica <span>▾</span></header><section className="chat">{messages.length===0?<div className="welcome"><h1>How can I help you?</h1><p>Ask a question, upload knowledge, or start a new conversation.</p></div>:messages.map((m,i)=><div className={'row '+m.role} key={i}><div className="bubble">{m.content}</div></div>)}{loading&&<div className="row assistant"><div className="bubble">Thinking…</div></div>}</section><div className="composer"><textarea value={input} onChange={e=>setInput(e.target.value)} onKeyDown={e=>{if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();send()}}} placeholder="Message ChatGPT…"/><button onClick={send}>↑</button></div><small>ChatGPT Replica can make mistakes. Check important information.</small></main></div>
}
