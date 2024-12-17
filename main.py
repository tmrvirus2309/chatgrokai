from openai import OpenAI
KEY_GROK = "xai-Y1FO0tB0up7nfMqlBdmS4HD0nRQxGs1n6sZPI1ldiwbzpl06kxkJkcvzvfMULVNgwDvYtCvFaTz3BmsV"
client = OpenAI(
    api_key=KEY_GROK,
    base_url="https://api.x.ai/v1",
)
def grok(ask):
    res = client.chat.completions.create(
        model="grok-beta",
        messages=[
            {"role": "system", "content": "Tên của bạn là Rov."},
            {"role": "user", "content": ask}
        ]
    )
    return res.choices[0].message.content
ask = input("Ask: ")
print(grok(ask))
