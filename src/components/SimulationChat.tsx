"use client";

import React, { useEffect, useRef } from "react";
import { motion } from "framer-motion";
import {
  Send,
  MoreVertical,
  Phone,
  Video,
  CheckCheck,
  ShieldAlert,
  Terminal,
  Activity
} from "lucide-react";

const transcript = [
  { id: "1", time: "2:50 pm", sender: "kori", text: "I don't punish you over your overthinking, you straight up said you decide when you'll meet me" },
  { id: "2", time: "2:51 pm", sender: "Sakshi", text: "Because you are literally absolutely okay with everything it means you don't want to put forward your opinions" },
  { id: "3", time: "2:52 pm", sender: "Sakshi", text: "Which I don't like at all" },
  { id: "4", time: "2:52 pm", sender: "Sakshi", text: "No one leaves anyone for speaking their mind" },
  { id: "5", time: "2:53 pm", sender: "Sakshi", text: "I don't want your mind to be in shackles or smthng or you just weigh everything around me" },
  { id: "6", time: "2:53 pm", sender: "Sakshi", text: "I don't want to see the perfect you" },
  { id: "7", time: "2:54 pm", sender: "Sakshi", text: "I want the true you" },
  { id: "8", time: "2:56 pm", sender: "Sakshi", text: "You literally say everything which is not of substance without overthinking but not your true calling" },
  { id: "9", time: "2:56 pm", sender: "Sakshi", text: "Why this partiality" },
  { id: "10", time: "2:58 pm", sender: "Sakshi", text: "And if you know me well then uk that I can't do that maybe you're okay with everything but I am not , you're okay with not meeting but I am not", replyTo: "I don't punish you over your overthinking, you straight up said you decide when you'll meet me" },
  { id: "11", time: "3:04 pm", sender: "kori", text: "that is the issue", replyTo: "I don't want to see the perfect you" },
  { id: "12", time: "3:05 pm", sender: "kori", text: "see in all honesty I want to meet you before classes" },
  { id: "13", time: "3:05 pm", sender: "kori", text: "not gonna wait till oct ik its a joke" },
  { id: "14", time: "3:05 pm", sender: "kori", text: "and I'll try to start being more honest" },
  { id: "15", time: "3:07 pm", sender: "kori", text: "you're mean for using my fear of abandonment as a leverage", replyTo: "Maybe october that we'll see if I am in the mood" },
  { id: "16", time: "3:07 pm", sender: "kori", text: "doesn't create a safe space in this relationsghip at all" },
  { id: "17", time: "3:08 pm", sender: "kori", text: "I have been passive, sure, but I want to negotiate more" },
  { id: "18", time: "3:08 pm", sender: "kori", text: "my genuine input right now is that I want to meet you before time" },
  { id: "19", time: "3:08 pm", sender: "Sakshi", text: "Do you really think that I said that srsly", replyTo: "you're mean for using my fear of abandonment as a leverage" },
  { id: "20", time: "3:08 pm", sender: "kori", text: "I DON'T KNOW", replyTo: "Do you really think that I said that srsly" },
  { id: "21", time: "3:08 pm", sender: "kori", text: "but it didn't feel right either" },
  { id: "22", time: "3:09 pm", sender: "kori", text: "tell me honestly, will you respect my preference when it differs from yours" },
  { id: "23", time: "3:09 pm", sender: "kori", text: "or would it only be applicable when I'm with you in an opinion" },
  { id: "24", time: "3:10 pm", sender: "Sakshi", text: "I am just trying to know you more and you being hesitant around i don't like it , you being hesitant and I am just accepting doesn't create a safe space like you think so", replyTo: "doesn't create a safe space in this relationsghip at all" },
  { id: "25", time: "3:11 pm", sender: "Sakshi", text: "Off course I will how can two peoples opinions be same , there are differences of opinions sometimes you have to sacrifice for my sake , sometimes I have to", replyTo: "tell me honestly, will you respect my preference when it differs from yours" },
  { id: "26", time: "3:11 pm", sender: "Sakshi", text: "You should not be the only one making sacrifices here" },
  { id: "27", time: "3:12 pm", sender: "kori", text: "there's also the fact that you keep testing me" },
  { id: "28", time: "3:12 pm", sender: "kori", text: "you question my attraction towards you, or the fact that" },
  { id: "29", time: "3:12 pm", sender: "kori", text: "why I chose you" },
  { id: "30", time: "3:13 pm", sender: "kori", text: "or my past" },
  { id: "31", time: "3:13 pm", sender: "kori", text: "yes you do mention that iit feels like you're interrogating me, I don't mind it" },
  { id: "32", time: "3:13 pm", sender: "kori", text: "but it shapes my other decisions like the fact that I never question your decision or just whole heartedly agree to everything" },
  { id: "33", time: "3:14 pm", sender: "kori", text: "I hve my oqn insecurities" },
  { id: "34", time: "3:16 pm", sender: "Sakshi", text: "That comes out of curiosity, I never meant to interrogate you or question you , but because it involves me I love to know about myself through your eyes", replyTo: "you question my attraction towards you, or the fact that" },
  { id: "35", time: "3:17 pm", sender: "Sakshi", text: "Like what", replyTo: "I hve my oqn insecurities" },
  { id: "36", time: "3:17 pm", sender: "kori", text: "everything dude", replyTo: "Like what" },
  { id: "37", time: "3:17 pm", sender: "kori", text: "everything" },
  { id: "38", time: "3:17 pm", sender: "kori", text: "it can be anything" },
  { id: "39", time: "3:17 pm", sender: "kori", text: "my brain my face my hands could be my feet, I'm not mperfect" },
  { id: "40", time: "3:18 pm", sender: "Sakshi", text: "Did I do something that made you insecure" },
  { id: "41", time: "3:18 pm", sender: "kori", text: "not you, it's inbuilt" },
  { id: "42", time: "3:19 pm", sender: "Sakshi", text: "Don't you think everyone has insecurities , tell me one person without insecurity", replyTo: "I hve my oqn insecurities" },
  { id: "43", time: "3:19 pm", sender: "kori", text: "whatever" },
  { id: "44", time: "3:19 pm", sender: "kori", text: "whatever" },
  { id: "45", time: "3:19 pm", sender: "kori", text: "anyways" },
  { id: "46", time: "3:20 pm", sender: "kori", text: "I'll do that" },
  { id: "47", time: "3:20 pm", sender: "kori", text: "I'll be more honest" },
  { id: "48", time: "3:20 pm", sender: "Sakshi", text: "Are you mad at me over smthng" },
  { id: "49", time: "3:20 pm", sender: "kori", text: "No why would I be mat at you" },
  { id: "50", time: "3:20 pm", sender: "kori", text: "im mad at everything around me, thats all" },
  { id: "51", time: "3:21 pm", sender: "kori", text: "and the fact that I gotta go to work tmrw" },
  { id: "52", time: "3:21 pm", sender: "kori", text: "and colle is starging thats all" },
  { id: "53", time: "3:22 pm", sender: "Sakshi", text: "Then it's ok" },
  { id: "54", time: "3:23 pm", sender: "kori", text: "yeah" },
  { id: "55", time: "3:23 pm", sender: "kori", text: "I got some questions for you if you don't mind" },
  { id: "56", time: "3:24 pm", sender: "kori", text: "just say yes or no" },
  { id: "57", time: "3:24 pm", sender: "Sakshi", text: "Yes" },
  { id: "58", time: "3:24 pm", sender: "kori", text: "are you happy with talking to me" },
  { id: "59", time: "3:24 pm", sender: "Sakshi", text: "Offcourse yes" },
  { id: "60", time: "3:24 pm", sender: "kori", text: "did I make you feel heard with my last message" },
  { id: "61", time: "3:24 pm", sender: "kori", text: "are you feeling frustrated with our conversation today" },
  { id: "62", time: "3:24 pm", sender: "kori", text: "do you feel understood by me" },
  { id: "63", time: "3:25 pm", sender: "Sakshi", text: "Last message about you try to be more honest ? Then yes", replyTo: "did I make you feel heard with my last message" },
  { id: "64", time: "3:27 pm", sender: "Sakshi", text: "Little bit because I always think we are going in circles and I am not able to create a space where you are comfortable speaking your mind or heart and you overthink", replyTo: "are you feeling frustrated with our conversation today" },
  { id: "65", time: "3:27 pm", sender: "kori", text: "Texting sucks, sit on my lap and ask me all the questions you want", replyTo: "Little bit because I always think we are going in circles and I am not able to create a space where you are comfortable speaking your mind or heart and you overthink" },
  { id: "66", time: "3:28 pm", sender: "Sakshi", text: "Sometimes I think you dont understand what I am trying to say", replyTo: "do you feel understood by me" },
  { id: "67", time: "3:28 pm", sender: "Sakshi", text: "I don't think you will answer anything that way 🙃", replyTo: "Texting sucks, sit on my lap and ask me all the questions you want" },
  { id: "68", time: "3:29 pm", sender: "kori", text: "hmm fair point", replyTo: "I don't think you will answer anything that way" },
  { id: "69", time: "3:29 pm", sender: "kori", text: "do you see potential for us to be more than just talking" },
  { id: "70", time: "3:30 pm", sender: "kori", text: "do you feel safe being vulnerable with me" },
  { id: "71", time: "3:31 pm", sender: "Sakshi", text: "Yes, I do", replyTo: "do you see potential for us to be more than just talking" },
  { id: "72", time: "3:31 pm", sender: "Sakshi", text: "Yess otherwise I won't be this vocal", replyTo: "do you feel safe being vulnerable with me" },
  { id: "73", time: "3:32 pm", sender: "kori", text: "do you trust that I'm being genuine with you" }
];

export default function SimulationChat() {
  const scrollRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to bottom on mount
  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, []);

  return (
    <div className="flex items-center justify-center min-h-screen bg-[#f1f5f9] p-4 sm:p-6 md:p-8 font-sans selection:bg-indigo-100/50">
      <div className="w-full max-w-3xl bg-[#f8fafc]/90 backdrop-blur-2xl border border-white/60 rounded-[2rem] shadow-[0_20px_60px_-15px_rgba(99,102,241,0.15)] overflow-hidden flex flex-col h-[85vh] relative before:absolute before:inset-0 before:bg-gradient-to-b before:from-white/40 before:to-transparent before:pointer-events-none">
        
        {/* Header - Clinical / Sci-fi Log Style */}
        <div className="h-16 px-6 border-b border-indigo-100/40 flex items-center justify-between bg-white/60 backdrop-blur-md z-10 sticky top-0 shrink-0 shadow-sm">
          <div className="flex items-center gap-4">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-indigo-50 to-cyan-50 border border-indigo-100/50 flex items-center justify-center text-indigo-500 shadow-sm shadow-indigo-100/50 rotate-3 transition-transform hover:rotate-0">
              <Terminal size={20} className="text-indigo-600" />
            </div>
            <div className="flex flex-col">
              <div className="flex items-center gap-2">
                <h2 className="text-slate-800 font-bold text-[13px] tracking-widest uppercase">Transcript Log</h2>
                <span className="px-1.5 py-0.5 rounded text-[9px] font-mono font-bold bg-indigo-100 text-indigo-700 tracking-wider">
                  CONFIDENTIAL
                </span>
              </div>
              <p className="text-[10px] font-mono text-slate-500 uppercase tracking-wider mt-0.5 flex items-center gap-1.5">
                <Activity size={10} className="text-cyan-500" /> 
                Participants: Sakshi // Kori
              </p>
            </div>
          </div>
          <div className="flex items-center gap-3">
            <div className="hidden sm:flex items-center gap-1.5 px-2.5 py-1.5 rounded-full bg-emerald-50/80 border border-emerald-100/80 shadow-sm">
              <div className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse shadow-[0_0_8px_rgba(52,211,153,0.8)]"></div>
              <span className="text-[9px] font-mono font-bold text-emerald-600 uppercase tracking-widest">Live Sync</span>
            </div>
            <button className="p-2 text-slate-400 hover:text-indigo-600 hover:bg-indigo-50 transition-colors rounded-full">
              <MoreVertical size={18} />
            </button>
          </div>
        </div>

        {/* Info banner */}
        <div className="bg-gradient-to-r from-transparent via-indigo-50/50 to-transparent border-b border-indigo-100/30 py-2.5 px-4 flex justify-center shrink-0">
          <div className="flex items-center gap-2 text-[10px] uppercase tracking-widest text-slate-500 font-mono font-semibold bg-white/80 px-4 py-1.5 rounded-full border border-indigo-100/50 shadow-sm">
            <ShieldAlert size={12} className="text-indigo-400" />
            End-to-end encrypted simulation environment
          </div>
        </div>

        {/* Chat Area */}
        <div 
          ref={scrollRef}
          className="flex-1 overflow-y-auto p-4 sm:p-6 md:p-8 space-y-5 scroll-smooth custom-scrollbar"
        >
          {transcript.map((msg, idx) => {
            const isKori = msg.sender === 'kori';
            const isFirstInGroup = idx === 0 || transcript[idx - 1].sender !== msg.sender;
            
            return (
              <motion.div 
                key={msg.id}
                initial={{ opacity: 0, y: 15, scale: 0.97 }}
                whileInView={{ opacity: 1, y: 0, scale: 1 }}
                viewport={{ root: scrollRef, once: true, margin: "100px" }}
                transition={{ duration: 0.4, ease: [0.23, 1, 0.32, 1], delay: (idx % 15) * 0.03 }}
                className={`flex flex-col ${isKori ? 'items-end' : 'items-start'} w-full`}
              >
                <div className={`flex flex-col ${isKori ? 'items-end' : 'items-start'} max-w-[88%] sm:max-w-[75%]`}>
                  
                  {isFirstInGroup && (
                    <div className={`flex items-baseline gap-2 mb-1.5 ${isKori ? 'flex-row-reverse' : 'flex-row'} px-1`}>
                      <span className="text-[10px] font-mono font-bold text-slate-400 uppercase tracking-widest">{msg.sender}</span>
                    </div>
                  )}

                  {msg.replyTo && (
                    <div className={`mb-1.5 relative px-3.5 py-2.5 text-[11px] rounded-xl backdrop-blur-sm shadow-sm ${
                      isKori 
                        ? 'bg-indigo-50/80 text-indigo-900/80 border border-indigo-200/50' 
                        : 'bg-white/60 text-slate-600/80 border border-slate-200/60'
                    }`}>
                      <div className={`absolute left-0 top-0 bottom-0 w-1 rounded-l-xl ${isKori ? 'bg-indigo-300' : 'bg-slate-300'}`}></div>
                      <div className="font-mono font-bold mb-1 text-[9px] uppercase tracking-widest opacity-60">
                        Replying to {isKori ? 'Sakshi' : 'Kori'}
                      </div>
                      <div className="line-clamp-2 italic leading-relaxed">{msg.replyTo}</div>
                    </div>
                  )}
                  
                  <div className={`relative px-4.5 py-3 text-[14px] leading-relaxed backdrop-blur-md transition-all hover:shadow-md ${
                    isKori 
                      ? `bg-indigo-50/90 border border-indigo-200/60 text-slate-800 shadow-sm shadow-indigo-100/50 rounded-2xl ${isFirstInGroup ? 'rounded-tr-sm' : ''}` 
                      : `bg-white/95 border border-slate-200/80 text-slate-700 shadow-sm shadow-slate-200/50 rounded-2xl ${isFirstInGroup ? 'rounded-tl-sm' : ''}`
                  }`}>
                    <span className="block whitespace-pre-wrap px-1">{msg.text}</span>
                    
                    <div className={`flex items-center gap-1.5 mt-2 px-1 ${
                      isKori ? 'justify-end' : 'justify-start'
                    }`}>
                      <span className="text-[9px] font-mono font-medium uppercase tracking-widest text-slate-400">
                        {msg.time}
                      </span>
                      {isKori && <CheckCheck size={13} className="text-indigo-400" />}
                    </div>
                  </div>
                </div>
              </motion.div>
            );
          })}
        </div>

        {/* Input Area */}
        <div className="p-4 sm:p-5 bg-white/70 backdrop-blur-xl border-t border-indigo-100/50 shrink-0 z-10">
          <div className="max-w-4xl mx-auto flex items-center gap-3">
            <button className="hidden sm:flex p-2.5 text-slate-400 hover:text-indigo-600 hover:bg-indigo-50 transition-colors rounded-full border border-transparent hover:border-indigo-100">
              <Terminal size={18} />
            </button>
            <div className="flex-1 flex items-center gap-2 bg-white/90 border border-slate-200 shadow-[0_2px_10px_-3px_rgba(0,0,0,0.05)] rounded-full p-1.5 pl-5 focus-within:border-indigo-300 focus-within:ring-4 focus-within:ring-indigo-100/50 transition-all">
              <div className="w-2 h-2 rounded-full bg-indigo-400 animate-pulse"></div>
              <input 
                type="text" 
                placeholder="Awaiting operator input..." 
                className="flex-1 bg-transparent border-none outline-none text-[13px] font-mono text-slate-700 placeholder:text-slate-400"
                readOnly
              />
              <button className="w-9 h-9 rounded-full bg-gradient-to-br from-indigo-500 to-cyan-500 flex items-center justify-center text-white shadow-md shadow-indigo-200 shrink-0 hover:scale-105 hover:shadow-lg transition-all">
                <Send size={15} className="ml-0.5" />
              </button>
            </div>
          </div>
        </div>

      </div>

      <style dangerouslySetInnerHTML={{__html: `
        .custom-scrollbar::-webkit-scrollbar {
          width: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
          background: transparent;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background-color: rgba(165, 180, 252, 0.3);
          border-radius: 10px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
          background-color: rgba(165, 180, 252, 0.5);
        }
      `}} />
    </div>
  );
}
