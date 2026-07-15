from database import supabase

try:
    response = supabase.table("cases").select("*").execute()

    print("✅ Supabase Connected Successfully")
    print(response.data)

except Exception as e:
    print("❌ Connection Failed")
    print(e)